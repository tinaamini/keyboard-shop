from django.urls import path
from .views import *

app_name="blogHome"
urlpatterns = [
    path('', home, name='home'),


]