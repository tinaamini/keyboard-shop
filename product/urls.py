from django.urls import path
from .views import  search, productDetail, latest_products,category_products

app_name = "productBlog"

urlpatterns = [
    path('products/<str:category_name>/',category_products, name='category_products'),
    path('search/', search, name='search'),
    path('detail/<int:id>/', productDetail, name='productDetail'),
    path('new-products/', latest_products, name='new_products'),


]
