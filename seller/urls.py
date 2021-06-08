from django.urls import path, include
from seller.views import Seller, index

urlpatterns = [
    path('', index),
    path('sellers/', Seller.as_view(), name='sellers'),
    path('sellers/<action>', Seller.as_view(), name='sellers'),
    path('sellers/<action>/<id>', Seller.as_view(), name='sellers'),
]