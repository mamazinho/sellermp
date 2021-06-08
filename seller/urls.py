from django.urls import path, include
from seller.views import Seller

urlpatterns = [
    path('', Seller.as_view()),
]