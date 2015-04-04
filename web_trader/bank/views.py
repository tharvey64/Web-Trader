from django.shortcuts import render, redirect
from django.views.generic import View
# from bank.forms import BankForm

# Create your views here.

class ViewAccount(View):
	template = 'bank/accounts.html'

	def get(self, request):
   		return render(request, self.template)

class ViewBanker(View):
	template = 'bank/banker.html'

	def get(self, request):
		return render(request, self.template)

	def post(self, request):
		return redirect('/')
