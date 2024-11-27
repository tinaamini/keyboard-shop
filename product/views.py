from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from .models import BaseProducts, Category
from django.db.models import CharField, Q
from .models import Value, ProductImage, Attributes
from .colors import COLOR_DICT
from django.views import View
from orders.forms import CartAddForm


# Create your views here

class ProductsView(View):
    def get(self, request, category_name=None, category_slug=None):
        products = BaseProducts.objects.filter(is_activated=True)
        # products_list = BaseProducts.objects.all()
        categories = Category.objects.filter(is_sub=False)
        # product_filter = BaseProducts.objects.filter(is_activated=True,slug=category_name)

        if category_slug:
            category = Category.objects.get(slug=category_slug)
            products = products.filter(category=category)
        return render(request, 'products/product_list.html',
                      {'products': products, 'categories': categories})


def search(request):
    search_term = request.GET.get('q', '')

    if search_term:
        fields = [f for f in BaseProducts._meta.fields if isinstance(f, CharField)]
        queries = [Q(**{f.name + '__icontains': search_term}) for f in fields]

        qs = Q()
        for query in queries:
            qs = qs | query

        results = BaseProducts.objects.filter(qs)

        # ارسال پیام مناسب در صورت عدم وجود نتیجه
        no_results = not results.exists()
    else:
        results = BaseProducts.objects.none()
        no_results = False

    return render(request, 'products/search_results.html', {'results': results, 'search_term': search_term})


def productDetail(request, id):
    product = get_object_or_404(BaseProducts, id=id)
    values = Value.objects.filter(product=product)
    images = ProductImage.objects.filter(product=product)
    # valuess = Value.objects.filter(product=product)
    # بازیابی ویژگی قیمت
    price_attribute = Attributes.objects.filter(title='قیمت').first()
    price_value = values.filter(attribute=price_attribute).first() if price_attribute else None
    price = price_value.value if price_value else 'N/A'
    # بازیابی رنگ‌ها برای فیلتر
    colors = Value.objects.filter(product=product, attribute__title='رنگ').values('colors')



    form = CartAddForm()

    context = {
        'product': product,
        'values': values,
        'images': images,
        'price': price,
        'form': form,
        'colors':colors

    }

    return render(request, 'products/product_detail.html', context)


def latest_products(request):
    # Gereftan 30 mahsule jadid
    products = BaseProducts.objects.order_by('-date_created')[:30]

    return render(request, 'home/new-products.html', {'all_products': products})
