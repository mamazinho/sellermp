from django.forms.models import model_to_dict
from django.shortcuts import redirect, render
from django.views import View

from marketplace.models import Marketplace as MMarketplace
from marketplace.models import MarketplaceForm
from marketplace.models import MarketplaceSettings as MMarketplaceSettings
from marketplace.models import MarketplaceSettingsForm


class Marketplace(View):
    form_market = MarketplaceForm
    template = "marketplace-form.html"

    def get(self, request, action=None, id=None):
        if action and action == "new":
            form = self.form_market
            return render(request, self.template, {"form": form})

        if action and action == "update" and id:
            return self.put(request, id)

        if action and action == "delete" and id:
            return self.delete(request, id)

        marketplaces = MMarketplace.objects.all()
        return render(request, "marketplace.html", {"marketplaces": marketplaces})

    def post(self, request, action=None, id=None):
        if id:
            data = MMarketplace.objects.get(id=id)
            form = self.form_market(request.POST, instance=data)
        else:
            form = self.form_market(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/marketplaces", id=id)

    def put(self, request, id=None):
        data = MMarketplace.objects.get(id=id)
        try:
            settings = MMarketplaceSettings.objects.all().filter(marketplace=id)
        except MMarketplaceSettings.DoesNotExist:
            settings = None

        form = self.form_market(initial=model_to_dict(data))
        return render(
            request, self.template, {"form": form, "settings": settings, "id": data.id}
        )

    def delete(self, request, id=None):
        data = MMarketplace.objects.get(id=id)
        data.delete()
        return redirect("marketplace")


class MarketplaceSettings(View):
    form_settings = MarketplaceSettingsForm
    template = "settings-form.html"

    def get(self, request, action=None, id=None):
        if action and action == "new":
            form = self.form_settings
            return render(request, self.template, {"form": form})

        if action and action == "update" and id:
            return self.put(request, id)

        if action and action == "delete" and id:
            return self.delete(request, id)

    def post(self, request, action=None, id=None):
        if id:
            data = MMarketplaceSettings.objects.get(id=id)
            form = self.form_settings(request.POST, instance=data)
        else:
            form = self.form_settings(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/marketplaces")

    def put(self, request, id=None):
        data = MMarketplaceSettings.objects.get(id=id)
        form = self.form_settings(initial=model_to_dict(data))
        return render(request, self.template, {"form": form})

    def delete(self, request, id=None):
        data = MMarketplaceSettings.objects.get(id=id)
        data.delete()
        return redirect("marketplace")
