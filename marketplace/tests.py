from django.test import TestCase

from marketplace.models import Marketplace as MMarketplace
from marketplace.models import MarketplaceForm
from marketplace.models import MarketplaceSettings as MMarketplaceSettings
from marketplace.models import MarketplaceSettingsForm


class MarketPlaceTest(TestCase):
    def test_marketplace(self):

        response = self.client.get("/marketplaces/")
        self.assertEqual(response.status_code, 200)

        form_data = {"name": "teste", "website": "teste", "active": True}
        form = MarketplaceForm(data=form_data)
        self.assertTrue(form.is_valid())

        response = self.client.get(
            "/marketplaces",
            action="new",
            id=None,
            kwargs={"name": "teste", "website": "teste", "active": True},
        )
        self.assertEqual(response.status_code, 301)

        response = self.client.post(
            "/marketplaces/new", {"name": "teste", "website": "teste", "active": True}
        )
        self.assertEqual(response.status_code, 302)

        marketplace = MMarketplace.objects.last()
        self.assertEqual(marketplace.id, 1)

        response = self.client.put(
            f"/marketplaces/update/{marketplace.id}",
            {"name": "teste updt", "website": "teste updt", "active": True},
        )
        self.assertEqual(response.status_code, 200)

        response = self.client.post(
            f"/marketplaces/update/{marketplace.id}",
            {"name": "teste updt", "website": "teste updt", "active": True},
        )
        self.assertEqual(response.status_code, 302)

        marketplace = MMarketplace.objects.last()
        self.assertEqual(marketplace.name, "teste updt")

        marketplace = MMarketplace.objects.last()
        response = self.client.get(
            f"/marketplaces/delete/{marketplace.id}", id=marketplace.id
        )
        self.assertEqual(response.status_code, 302)

        marketplace = MMarketplace.objects.last()
        self.assertFalse(marketplace)


class MarketplaceSettingsTest(TestCase):
    def setUp(self):
        self.id = MMarketplace.objects.create(
            name="teste", website="teste", active=True
        ).id
        self.form_data = {
            "api": "teste",
            "endpoint": "teste",
            "secret_key": "teste",
            "marketplace": self.id,
        }
        self.form_data_update = {
            "api": "teste updt",
            "endpoint": "teste",
            "secret_key": "teste",
            "marketplace": self.id,
        }

    def test_marketplace_settings(self):

        form = MarketplaceSettingsForm(data=self.form_data)
        self.assertTrue(form.is_valid())

        response = self.client.post("/marketplaces/settings/new/", self.form_data)
        self.assertEqual(response.status_code, 302)

        settings = MMarketplaceSettings.objects.last()
        self.assertEqual(settings.id, 1)

        response = self.client.put(
            f"/marketplaces/settings/update/{settings.id}", self.form_data
        )
        self.assertEqual(response.status_code, 200)

        response = self.client.post(
            f"/marketplaces/settings/update/{settings.id}", self.form_data_update
        )
        self.assertEqual(response.status_code, 302)

        settings = MMarketplaceSettings.objects.last()
        self.assertEqual(settings.api, "teste updt")

        settings = MMarketplaceSettings.objects.last()
        response = self.client.get(
            f"/marketplaces/settings/delete/{settings.id}", id=settings.id
        )
        self.assertEqual(response.status_code, 302)

        settings = MMarketplaceSettings.objects.last()
        self.assertFalse(settings)
