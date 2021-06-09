from django.test import TestCase

from seller.models import Seller as MSeller
from seller.models import SellerContact as MDetail


class SellerTestCase(TestCase):
    def setUp(self):
        self.seller = {
            "cnpj": "12345678",
            "company_name": "testolist",
            "bank_name": "testbank",
            "bank_account": 123456,
            "bank_agency": 1000,
        }

        self.seller_update = self.seller
        self.seller_update["company_name"] = "olisttest"

    def test_get_list_sellers_template_in_seller_api(self):
        response = self.client.get("/sellers/")
        self.assertEqual(response.status_code, 200)

    def test_get_create_form_template_in_seller_api(self):
        response = self.client.get("/sellers/new")
        self.assertEqual(response.status_code, 200)

    def test_post_create_seller_in_seller_api(self):
        response = self.client.post("/sellers/new", self.seller)
        self.assertEqual(response.status_code, 302)

    def test_get_update_form_template_in_seller_api(self):
        self.client.post("/sellers/new", self.seller)
        last_seller = MSeller.objects.last()
        response = self.client.get(f"/sellers/update/{last_seller.id}")
        self.assertEqual(response.status_code, 200)

    def test_patch_seller_in_seller_api(self):
        self.client.post("/sellers/new", self.seller)
        last_seller = MSeller.objects.last()
        response = self.client.post(
            f"/sellers/update/{last_seller.id}", self.seller_update
        )
        self.assertEqual(response.status_code, 302)

    def test_delete_seller_in_seller_api(self):
        self.client.post("/sellers/new", self.seller)
        last_seller = MSeller.objects.last()
        # Test get because front makes this request, reason: unsupported delete in html
        response = self.client.get(f"/sellers/delete/{last_seller.id}")
        self.assertEqual(response.status_code, 302)


class SellerContactTestCase(TestCase):
    def setUp(self):
        MSeller.objects.create(
            cnpj="12345678",
            company_name="testolist",
            bank_name="testbank",
            bank_account=123456,
            bank_agency=1000,
        )
        self.last_seller = MSeller.objects.last()
        self.seller_details = {
            "address": "rua teste",
            "seller_id": self.last_seller.id,
            "responsible_email": "teste@test.com",
            "phone_number": 4199998888,
        }

        self.seller_details_update = self.seller_details
        self.seller_details_update["address"] = "teste de rua"

    def test_get_create_form_template_in_details_api(self):
        response = self.client.get(
            "/sellers/seller-details/new", {"seller_id": self.last_seller.id}
        )
        self.assertEqual(response.status_code, 200)

    def test_post_create_detail_in_details_api(self):
        response = self.client.post(
            f"/sellers/seller-details/new?seller_id={self.last_seller.id}",
            self.seller_details,
        )
        self.assertEqual(response.status_code, 302)

    def test_get_update_form_template_in_details_api(self):
        self.client.post(
            f"/sellers/seller-details/new?seller_id={self.last_seller.id}",
            self.seller_details,
        )
        last_detail = MDetail.objects.last()
        response = self.client.get(
            f"/sellers/seller-details/update/{last_detail.id}?seller_id={self.last_seller.id}",
            self.seller_details_update,
        )
        self.assertEqual(response.status_code, 200)

    def test_patch_detail_in_details_api(self):
        self.client.post(
            f"/sellers/seller-details/new?seller_id={self.last_seller.id}",
            self.seller_details,
        )
        last_detail = MDetail.objects.last()
        response = self.client.post(
            f"/sellers/seller-details/update/{last_detail.id}",
            self.seller_details_update,
        )
        self.assertEqual(response.status_code, 302)

    def test_delete_detail_in_details_api(self):
        self.client.post(
            f"/sellers/seller-details/new?seller_id={self.last_seller.id}",
            self.seller_details,
        )
        last_detail = MDetail.objects.last()
        # Test get because front makes this request, reason: unsupported delete in html
        response = self.client.get(f"/sellers/seller-details/delete/{last_detail.id}")
        self.assertEqual(response.status_code, 302)
