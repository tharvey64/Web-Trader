from django.shortcuts import render, redirect
from django.views.generic import View
from users.models import User
from accounts.models import Account
# from bank.forms import BankForm

# Create your views here.

class ViewIndex(View):
	template = 'bank/welcome.html'

	def get(self,request):
		user = User.objects.filter(id=request.session['user_id'])
		if len(user) == 1:
			return render(request, self.template, {'user':user[0]})
		return redirect('/users/')

class ViewAccount(View):
	template = 'bank/accounts.html'

	def get(self, request):
   		return render(request, self.template)

class ViewBanker(View):
	template = 'bank/banker.html'

	def get(self, request):
		return render(request, self.template)

	def post(self, request):
		new_account = Account()
		new_client = BankClient()
		new_b_account = BankAccount()
		new_account.type_of = request.POST['type_of']
		new_account.number = new_account.generate_account_number()
		return redirect('/bank/')
