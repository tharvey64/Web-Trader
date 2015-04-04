from django.shortcuts import render, redirect
from django.views.generic import View
from users.models import User
# from bank.forms import BankForm

# Create your views here.

class ViewIndex(View):
	template = 'bank/welcome.html'

	def get(self,request):
		user = User.objects.all().get(id=request.session['user_id'])
		return render(request, self.template, {'user':user})

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
