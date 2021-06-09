from django.urls import path

from seller.views import Detail, Seller

urlpatterns = [
    path("", Seller.as_view(), name="sellers"),
    path("seller-details/<action>", Detail.as_view(), name="seller-details"),
    path("seller-details/<action>/<id>", Detail.as_view(), name="seller-details"),
    path("<action>", Seller.as_view(), name="sellers"),
    path("<action>/<id>", Seller.as_view(), name="sellers"),
]
