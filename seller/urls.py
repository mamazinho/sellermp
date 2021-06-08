from django.urls import path

from seller.views import Seller, index

urlpatterns = [
    path("", index),
    path("seller/", Seller.as_view(), name="sellers"),
]
