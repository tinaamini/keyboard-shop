from django.shortcuts import render, get_object_or_404
from .models import BaseProducts
from django.db.models import CharField, Q
from .models import Value,ProductImage, Attributes
# Create your views here


def product_list(request, category):
    products = BaseProducts.objects.filter(category=category)
    categories = BaseProducts.objects.all()
    return render(request, 'products/product_list.html', {'products': products, 'categories': categories})


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
    price_attribute = Attributes.objects.filter(title='قیمت').first()

    price_value = values.filter(attribute=price_attribute).first() if price_attribute else None
    price = price_value.value if price_value else 'N/A'

    context = {
        'product': product,
        'values': values,
        'images': images,
        'price': price
    }

    return render(request, 'products/product_detail.html', context)
