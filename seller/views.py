from django.shortcuts import render
from django.views import View

# Create your views here.
def index(request):
    return render(request, 'base.html')

class Seller(View):
    
    def get(self, request):
        print('reeeq', request)
        return render(request, 'sellers.html')


    def post(self, request):
        pass


    def patch(self, request):
        pass

    def delete(self, request):
        pass