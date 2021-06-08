from django.shortcuts import render

from django.views import View

class MarketPlace(View):
    
    def get(self, request):
        print('reeeq', request)
        return render(request, 'base.html')


    def post(self, request):
        pass


    def patch(self, request):
        pass

    def delete(self, request):
        pass