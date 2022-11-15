from django.contrib import admin
from django.urls import path, include
from DZ_15_11_22.views import add_product, info_product

urlpatterns = [
    path('add/<str:product>, <int:price>/', add_product),
    path('info/<str:product>/', info_product),
]
