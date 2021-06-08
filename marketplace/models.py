from django.db import models
from django.forms import ModelForm


class Marketplace(models.Model):
    name = models.CharField(max_length=200)
    website = models.CharField(max_length=100)
    active = models.BooleanField(default=True)

    def __str__(self):
        return "{}".format(self.name)


class MarketplaceSettings(models.Model):
    marketplace = models.ForeignKey(Marketplace, on_delete=models.CASCADE)
    secret_key = models.CharField(max_length=200)
    api = models.CharField(max_length=200, default="")
    endpoint = models.CharField(max_length=200, default="")


class MarketplaceForm(ModelForm):
    class Meta:
        model = Marketplace
        fields = ["name", "website", "active"]


class MarketplaceSettingsForm(ModelForm):
    class Meta:
        model = MarketplaceSettings
        fields = ["marketplace", "secret_key", "api", "endpoint"]
