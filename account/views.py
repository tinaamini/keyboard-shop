from django.shortcuts import render, redirect
from django.views import View
from .forms import UserRegistrationForm, VerifyCodeForm, UserLoginForm
import random
from .models import OtpCode, User
from utils import send_otp_code
from django.contrib import messages
from django.utils import timezone
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.
class UserRegisterView(View):
    form_class = UserRegistrationForm

    def get(self, request):
        form = self.form_class
        return render(request, 'account/register.html', {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            random_code = random.randint(1000, 9999)
            send_otp_code(form.cleaned_data['phone'], random_code)
            OtpCode.objects.create(phone_number=form.cleaned_data['phone'], code=random_code)
            request.session['user_registration_info'] = {
                'phone_number': form.cleaned_data['phone'],
                'email': form.cleaned_data['email'],
                'full_name': form.cleaned_data['full_name'],
                'password': form.cleaned_data['password'],

            }
            messages.success(request, 'کدی به شماره همراه شما ارسال شد.', 'success')
            return redirect('accounts:verify_code')
        messages.error(request, 'فیلد ها صحیح وارد نشده اند.', 'error')
        return render(request, 'account/register.html', {"form": form})


class UserRegisterVerifyCodeView(View):
    form_class = VerifyCodeForm

    def get(self, request):
        form = self.form_class
        return render(request, 'account/verify_code.html', {'form': form})

    def post(self, request):
        user_session = request.session['user_registration_info']
        code_instance = OtpCode.objects.get(phone_number=user_session['phone_number'])
        form = self.form_class(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            expiration_time = code_instance.created + timezone.timedelta(minutes=5)
            if expiration_time > timezone.now():
                if cd['code'] == code_instance.code:
                    User.objects.create_user(
                        user_session['phone_number'],
                        user_session['email'],
                        user_session['full_name'],
                        user_session['password'],

                    )

                    code_instance.delete()
                    messages.success(request, 'ثبت نام شما با موفقیت انجام شد', 'success')
                    return redirect('blogHome:home')
                else:
                    messages.error(request, 'کد شما اشتباه است', 'danger')
                    return redirect('accounts:verify_code')
            else:
                messages.error(request, 'کد شما منقضی شده است ,لطفا دوباره امتحان کنید.', 'danger')
                code_instance.delete()
                return redirect('accounts:verify_code')

        return redirect('accounts:verify_code')


class UserLogoutView(LoginRequiredMixin, View):

    def get(self, requests):
        logout(requests)
        messages.success(requests, 'شما با موفقیت خارج شدید')
        return redirect('blogHome:home')


class UserLoginView(View):
    form_class = UserLoginForm
    template_name = 'account/login.html'

    def get(self, request):
        form = self.form_class
        return render(request, self.template_name, {"form": form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            cd = form.cleaned_data

            user = authenticate(request, phone_number=cd['phone'], password=cd['password'])

            if user is not None:
                login(request, user)
                messages.success(request, 'شما با موفقیت وارد شدید')

                return redirect('blogHome:home')

            messages.success(request, 'شما با وارد نشدید')
        return render(request, self.template_name, {'form': form})
