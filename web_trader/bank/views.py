from decimal import Decimal
from django.shortcuts import render, redirect
from django.views.generic import View
from users.models import User
from accounts.models import Account
from bank.models import BankClient, BankAccount

# Create your views here.
class NewClientView(View):
    template = 'bank/new_client.html'

    def get(self,request):
        return render(request, self.template)

    def post(self, request):
        current_user = User.objects.filter(id=request.session['user_id'])
        if len(current_user) == 1:
            BankClient.objects.create(user=current_user[0])
        return redirect('/bank/')		

class IndexView(View):
    template = 'bank/welcome.html'

    def get(self,request):
        bank_client = BankClient.objects.filter(user__pk=request.session['user_id'])
        if len(bank_client) == 1:
            request.session['bank_client_id'] = bank_client[0].id
            return render(request, self.template)
        return redirect('new_client/')

class AccountView(View):
    template = 'bank/accounts.html'

    def get(self, request):
        info = BankAccount.objects.filter(client__pk=request.session['bank_client_id'])
        return render(request, self.template, {'bank_client':info})

class BankerView(View):
    template = 'bank/banker.html'

    def get(self, request):
        return render(request, self.template)

    def post(self, request): 
        BankAccount.objects.create(
            client=BankClient.objects.get(
                id=request.session['bank_client_id']
            ),
            account=Account.objects.create(),
            type_of=request.POST['type_of'],
        )
        return redirect('/bank/')

class WithdrawView(View):
    template = 'bank/withdraw.html'

    def get(self, request):
        info = BankAccount.objects.filter(client__pk=request.session['bank_client_id'])		
        return render(request, self.template, {'accounts': info})

    def post(self, request):
        if request.POST['amount'].isdigit():
            current = BankAccount.objects.filter(account__number=request.POST['account'])
            if len(current) == 1:
                current[0].account.withdraw(Decimal(request.POST['amount']))
        return redirect('/bank/')

class DepositView(View):
    template = 'bank/deposit.html'

    def get(self, request):
        info = BankAccount.objects.filter(client__pk=request.session['bank_client_id'])		
        return render(request, self.template, {'accounts': info})

    def post(self, request):
        if request.POST['amount'].isdigit():
            current = BankAccount.objects.filter(account__number=request.POST['account'])
            if len(current) == 1:
                current[0].account.deposit(Decimal(request.POST['amount']))
        return redirect('/bank/')

class TransferView(View):
    template = 'bank/transfer.html'

    def get(self, request):
        info = BankAccount.objects.filter(client__pk=request.session['bank_client_id'])		
        return render(request, self.template, {'accounts': info})

    def post(self, request):
        if request.POST['amount'].isdigit():
            withdraw_from = BankAccount.objects.filter(account__number=request.POST['withdraw'])
            deposit_to = BankAccount.objects.filter(account__number=request.POST['deposit'])
            if len(withdraw_from) == 1 and len(deposit_to) == 1:
                if withdraw_from[0].account.withdraw(Decimal(request.POST['amount'])):
                    deposit_to[0].account.deposit(Decimal(request.POST['amount']))
        return redirect('/bank/')