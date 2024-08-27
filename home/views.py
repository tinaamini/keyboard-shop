from django.shortcuts import render
from product.models import BaseProducts

from django.core.paginator import Paginator


# Create your views here.


def home(request):
    products = BaseProducts.objects.order_by('-date_created')[:5]

    return render(request, 'templates/home/home.html', {'latest_products': products})
