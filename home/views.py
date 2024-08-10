from django.shortcuts import render

from django.core.paginator import Paginator



# Create your views here.


def home(request):



    return render(request, 'templates/home/home.html')