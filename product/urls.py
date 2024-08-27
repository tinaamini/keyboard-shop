from django.urls import path
from .views import product_list, search, productDetail, latest_products

app_name = "productBlog"

urlpatterns = [
    path('products/<str:category>/', product_list, name='product_list'),
    path('search/', search, name='search'),
    path('detail/<int:id>/', productDetail, name='productDetail'),
    path('new-products/', latest_products, name='new_products'),


]
