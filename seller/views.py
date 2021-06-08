from django.shortcuts import render, redirect
from django.views import View
from seller.models import Seller as MSeller

# Create your views here.
def index(request):
    return render(request, 'base.html')

class Seller(View):
    
    def get(self, request, action=None, id=None):
        if action:
            if action == 'new':
                return render(request, 'sellers-form.html')
            elif action == 'update':
                seller = MSeller.objects.get(id=id)
                return render(request, 'sellers-form.html', {'seller': seller})
            elif action == 'delete':
                self.delete(request, id)

        sellers = MSeller.objects.all()
        return render(request, 'sellers.html', {'sellers': sellers})


    def post(self, request, action=None, id=None):
        data = request.POST
        if id:
            self.patch(request, id)
        else:
            MSeller.objects.create(
                cnpj=data.get('cnpj'),
                company_name=data.get('company_name'),
                bank_name=data.get('bank_name'),
                bank_account=data.get('bank_account'),
                bank_agency=data.get('bank_agency'),
            )

        return redirect('sellers')


    def patch(self, request, id=None):
        data = request.POST
        seller = MSeller.objects.get(id=id)

        seller.cnpj = data.get('cnpj', seller.cnpj)
        seller.company_name = data.get('company_name', seller.company_name)
        seller.bank_name = data.get('bank_name', seller.bank_name)
        seller.bank_account = data.get('bank_account', seller.bank_account)
        seller.bank_agency = data.get('bank_agency', seller.bank_agency)

        seller.save()
        return redirect('sellers')

    def delete(self, request, id=None):
        MSeller.objects.get(id=id).delete()
        return redirect('sellers')