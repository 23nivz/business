from django.urls import path
from .views import *


urlpatterns = [
    path('',Home,name='home'),
    path('search',Search,name='search')
]