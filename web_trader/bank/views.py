from django.shortcuts import render
from django.views.generic import View
from bank.forms import BankForm
from users.models import User

# Create your views here.

class ViewAccount(View):
	form_class = BankForm
	

    def get(self, request):
    	return render(request, self.template)