from django.shortcuts import render, redirect
from django.views.generic import View
from stocks.models import Company,Markit
# Create your views here.

class IndexView(View):
    template = 'stocks/index.html'

    def get(self, request):
        return render(request, self.template)

class CompanySearchView(View):
    template = 'stocks/company_search.html'

    def get(self, request):
        return render(request,self.template)

    def post(self, request):
        search = request.POST['search_term']
        results = Markit.find_company(search)
        return render(request,self.template, {'search_results': results})

class QuoteView(View):
    template = 'stocks/stock_quote.html'

    def get(self, request):
        return render(request,self.template)

    def post(self, request):
        symbol = request.POST['symbol']
        result = Markit.find_quote(symbol)
        return render(request,self.template, {'stock_quote': result})