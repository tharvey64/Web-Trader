from django.shortcuts import render, redirect
from django.views.generic import View
from users.models import User
from accounts.models import Account
from brokerage.models import BrokerageClient, BrokerageAccount
# from brokerage.forms import BankForm.

class IndexView(View):
    template = 'brokerage/index.html'

    def get(self,request):
        brokerage_client = BrokerageClient.objects.filter(
            user__pk=request.session['user_id']
        )
        if len(brokerage_client) == 1:
            user = User.objects.get(id=request.session['user_id'])
            request.session['brokerage_client_id'] = brokerage_client[0].id
            return render(request, self.template, {'user':user})
        return redirect('new_client/')

class NewClientView(View):
    template = 'brokerage/new_client.html'

    def get(self,request):
        current_user = request.session['user_id']   
        user = User.objects.get(id=current_user) 
        return render(request, self.template, {'user':user})

    def post(self, request):
        current_user = request.session['user_id']   
        user = User.objects.get(id=current_user) 
        new_client = BrokerageClient.objects.create(user=user)
        return redirect('/brokerage/')       

#Empty 
class AccountView(View):
    template = 'brokerage/accounts.html'

    def get(self, request):
        client_id = request.session['brokerage_client_id']
        accounts = BrokerageAccount.objects.filter(client__pk=client_id)
        print(accounts)
        return render(request, self.template, {'accounts': accounts})

class BrokerView(View):
    template = 'brokerage/create_account.html'

    def get(self, request):
        return render(request, self.template)

    def post(self, request):
        client = BrokerageClient.objects.get(
            id=request.session['brokerage_client_id'])
        new_account = Account.objects.create()
        brokerage_account = BrokerageAccount.objects.create(
            client=client,
            account=new_account)
        return redirect('/brokerage/')

class ViewWithdraw(View):
    template = 'brokerage/withdraw.html'

    def get(self, request):
        info = BrokerageAccount.objects.filter(client__pk=request.session['brokerage_client_id'])     
        return render(request, self.template, {'accounts': info})

    def post(self, request):
        account = BrokerageAccount.objects.filter(account__number=request.POST['account'])
        if len(account) == 1:
            account[0].account.withdraw(int(request.POST['amount']))
        return redirect('/brokerage/')

class ViewDeposit(View):
    template = 'brokerage/deposit.html'

    def get(self, request):
        info = BrokerageAccount.objects.filter(client__pk=request.session['brokerage_client_id'])     
        return render(request, self.template, {'accounts': info})

    def post(self, request):
        account = BrokerageAccount.objects.filter(account__number=request.POST['account'])
        if len(account) == 1:
            account[0].account.deposit(int(request.POST['amount']))
        return redirect('/brokerage/')        