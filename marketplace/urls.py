from django.urls import path
from marketplace.views import MarketPlace

urlpatterns = [
    path('', MarketPlace.as_view(), name='marketplace'),
]