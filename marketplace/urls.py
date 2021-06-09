from django.urls import path

from marketplace.views import Marketplace, MarketplaceSettings

urlpatterns = [
    path("", Marketplace.as_view(), name="marketplace"),
    path("settings/<action>/", MarketplaceSettings.as_view(), name="settings"),
    path("settings/<action>/<id>", MarketplaceSettings.as_view(), name="settings"),
    path("<action>", Marketplace.as_view(), name="marketplace"),
    path("<action>/<id>", Marketplace.as_view(), name="marketplace"),
]
