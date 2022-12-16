from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('', homepage,name="index"),
    path('insert', insert,name="insert"),
    path('search', search,name="search"),
    
    
]
