from django.shortcuts import render, redirect
from django.views.generic import View
from stocks.models import Company,Markit
# Create your views here.

class IndexView(View):
    template = 'stocks/index.html'

    def get(self, request):
        return render(request, self.template)