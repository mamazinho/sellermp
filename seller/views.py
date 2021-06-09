from django.shortcuts import redirect, render
from django.views import View

from seller.models import Seller as MSeller
from seller.models import SellerContact as MDetail


def index(request):
    return render(request, "base.html")


class Seller(View):
    def get(self, request, action=None, id=None):
        if action:
            if action == "new":
                return render(request, "sellers-form.html")
            elif action == "update":
                seller = MSeller.objects.get(id=id)
                details = seller.contacts.all()
                return render(
                    request, "sellers-form.html", {"seller": seller, "details": details}
                )
            elif action == "delete":
                return self.delete(request, id)

        sellers = MSeller.objects.all()
        return render(request, "sellers.html", {"sellers": sellers})

    def post(self, request, action=None, id=None):
        data = request.POST
        if id:
            self.patch(request, id)
        else:
            MSeller.objects.create(
                cnpj=data.get("cnpj"),
                company_name=data.get("company_name"),
                bank_name=data.get("bank_name"),
                bank_account=data.get("bank_account"),
                bank_agency=data.get("bank_agency"),
            )

        return redirect("sellers")

    def patch(self, request, id=None):
        data = request.POST
        seller = MSeller.objects.get(id=id)

        seller.cnpj = data.get("cnpj", seller.cnpj)
        seller.company_name = data.get("company_name", seller.company_name)
        seller.bank_name = data.get("bank_name", seller.bank_name)
        seller.bank_account = data.get("bank_account", seller.bank_account)
        seller.bank_agency = data.get("bank_agency", seller.bank_agency)

        seller.save()
        return redirect("sellers")

    def delete(self, request, id):
        MSeller.objects.get(id=id).delete()
        return redirect("sellers")


class Detail(View):
    def get(self, request, action, id=None):
        seller_id = request.GET.get("seller_id")

        if action == "new":
            return render(request, "details-form.html", {"seller_id": seller_id})

        if action == "update":
            detail = MDetail.objects.get(id=id)
            return render(
                request, "details-form.html", {"detail": detail, "seller_id": seller_id}
            )

        if action == "delete":
            return self.delete(request, id, seller_id)

    def post(self, request, action=None, id=None):
        data = request.POST
        if id:
            self.patch(request, id)
        else:
            MDetail.objects.create(
                address=data.get("address"),
                seller_id=data.get("seller_id"),
                responsible_email=data.get("responsible_email"),
                phone_number=data.get("phone_number"),
            )

        return redirect("sellers", action="update", id=data.get("seller_id"))

    def patch(self, request, id=None):
        data = request.POST
        detail = MDetail.objects.get(id=id)

        detail.address = data.get("address", detail.address)
        detail.responsible_email = data.get(
            "responsible_email", detail.responsible_email
        )
        detail.phone_number = data.get("phone_number", detail.phone_number)

        detail.save()
        return redirect("sellers", action="update", id=data.get("seller_id"))

    def delete(self, request, id, seller_id=None):
        MDetail.objects.get(id=id).delete()
        return redirect("sellers", action="update", id=seller_id)
