from django.urls import path

from seller.views import Detail, Seller, index

urlpatterns = [
    path("", index),
    path("sellers/", Seller.as_view(), name="sellers"),
    path("sellers/<action>", Seller.as_view(), name="sellers"),
    path("sellers/<action>/<id>", Seller.as_view(), name="sellers"),
    path("seller-details/<action>", Detail.as_view(), name="seller-details"),
    path("seller-details/<action>/<id>", Detail.as_view(), name="seller-details"),
]
