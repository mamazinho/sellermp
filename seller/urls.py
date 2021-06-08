from django.urls import path, include
from seller.views import Seller, index

urlpatterns = [
    path('', index),
    path('seller/', Seller.as_view(), name='sellers'),
]