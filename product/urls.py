from . import views
from django.urls import path
from .views import search, productDetail, latest_products, ProductsView

app_name = "productBlog"

urlpatterns = [
    path('search/', search, name='search'),
    path('detail/<int:id>/', productDetail, name='productDetail'),
    path('new-products/', latest_products, name='new_products'),
    path('category/<slug:category_slug>/', views.ProductsView.as_view(), name='category_filter')

]
