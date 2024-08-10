from django.urls import path
from .views import product_list, search, productDetail

app_name = "productBlog"

urlpatterns = [
    path('products/<str:category>/', product_list, name='product_list'),
    path('search/', search, name='search'),
    path('detail/<int:id>/', productDetail, name='productDetail'),
]
