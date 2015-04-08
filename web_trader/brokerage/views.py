from decimal import Decimal
from django.shortcuts import render, redirect
from django.views.generic import View
from django.db.models import Sum
from users.models import User
from accounts.models import Account
from brokerage.models import BrokerageClient, BrokerageAccount, Transaction
from stocks.models import Company,Markit

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
 
class AccountMenuView(View):
    template = 'brokerage/account_menu.html'

    def get(self, request):
        return render(request, self.template)

class AccountView(View):
    template = 'brokerage/accounts.html'

    def get(self, request):
        client_id = request.session['brokerage_client_id']
        accounts = BrokerageAccount.objects.filter(client__pk=client_id)
        return render(request, self.template, {'bank_client': accounts})

class BrokerView(View):
    template = 'brokerage/create_account.html'

    def get(self, request):
        return render(request, self.template)

    def post(self, request):
        client = BrokerageClient.objects.get(
            id=request.session['brokerage_client_id']
        )
        new_account = Account.objects.create()
        brokerage_account = BrokerageAccount.objects.create(
            client=client,
            account=new_account
        )
        return redirect('/brokerage/')

class WithdrawView(View):
    template = 'brokerage/withdraw.html'

    def get(self, request):
        info = BrokerageAccount.objects.filter(client__pk=request.session['brokerage_client_id'])     
        return render(request, self.template, {'accounts': info})

    def post(self, request):
        if request.POST['amount'].isdigit():
            current = BrokerageAccount.objects.filter(account__number=request.POST['account'])
            if len(current) == 1:
                success = current[0].account.withdraw(Decimal(request.POST['amount']))
        return redirect('/brokerage/')

class DepositView(View):
    template = 'brokerage/deposit.html'

    def get(self, request):
        info = BrokerageAccount.objects.filter(client__pk=request.session['brokerage_client_id'])     
        return render(request, self.template, {'accounts': info})

    def post(self, request):
        if request.POST['amount'].isdigit():
            current = BrokerageAccount.objects.filter(account__number=request.POST['account'])
            if len(current) == 1:
                current[0].account.deposit(Decimal(request.POST['amount']))
        return redirect('/brokerage/')        

class TransferView(View):
    template = 'brokerage/transfer.html'

    def get(self, request):
        info = BrokerageAccount.objects.filter(client__pk=request.session['brokerage_client_id'])     
        return render(request, self.template, {'accounts': info})

    def post(self, request):
        if request.POST['amount'].isdigit():
            withdraw_from = BrokerageAccount.objects.filter(account__number=request.POST['withdraw'])
            deposit_to = BrokerageAccount.objects.filter(account__number=request.POST['deposit'])
            if len(withdraw_from) == 1 and len(deposit_to) == 1:
                if withdraw_from[0].account.withdraw(Decimal(request.POST['amount'])):
                    deposit_to[0].account.deposit(Decimal(request.POST['amount']))
        return redirect('/brokerage/')

class PortfolioMenuView(View):
    template = 'brokerage/portfolio_menu.html'
    
    def get(self, request):
        return render(request, self.template)

class PortfolioView(View):
    template = 'brokerage/portfolio.html'

    def get(self, request):
        client_id = request.session['brokerage_client_id']
        transaction_history = Transaction.objects.filter(client__pk=client_id).values('company__symbol').annotate(owned=Sum('quantity')).order_by('owned')
        portfolio = transaction_history.filter(owned__gt=0)
        if len(portfolio) > 0:
            for company in portfolio:
                company['share_price'] = Markit.find_quote(company['company__symbol'])['LastPrice']
                company['value'] = company['share_price'] * company['owned']
            return render(request, self.template, {'portfolio': portfolio})
        return render(request, self.template)

class PurchaseView(View):
    template = 'brokerage/purchase.html'

    def get(self, request):
        client_id = request.session['brokerage_client_id']
        accounts = BrokerageAccount.objects.filter(client__pk=client_id)
        return render(request, self.template, {'accounts': accounts})

    def post(self, request):
        if request.POST['quantity'].isdigit():
            symbol = request.POST['symbol']
            quote = Markit.find_quote(symbol)
            if 'Message' not in quote:
                quantity = int(request.POST['quantity'])
                total_value = Decimal(quote['LastPrice']) * quantity
                account = BrokerageAccount.objects.filter(account__number=request.POST['account_num'])
                if len(account) == 1 and account[0].account.withdraw(total_value):
                    client = BrokerageClient.objects.get(id=request.session['brokerage_client_id'])
                    company,created = Company.objects.get_or_create(
                        symbol=quote['Symbol'],
                        name=quote['Name']
                    )
                    transaction = Transaction.objects.create(
                        company=company,
                        client=client,
                        quantity=quantity,
                        share_price=int(quote['LastPrice'])
                    )
                    return render(request, self.template, {'transaction': transaction})
        return redirect(request, self.template)

class SellView(View):
    template = 'brokerage/sell.html'

    def get(self, request):
        client_id = request.session['brokerage_client_id']
        accounts = BrokerageAccount.objects.filter(client__pk=client_id)
        return render(request, self.template, {'accounts': accounts})

    def post(self, request):
        if request.POST['quantity'].isdigit():
            symbol = request.POST['symbol']
            quote = Markit.find_quote(symbol)
            if 'Message' not in quote:
                quantity = int(request.POST['quantity'])
                total_value = Decimal(quote['LastPrice']) * quantity
                account = BrokerageAccount.objects.filter(account__number=request.POST['account_num'])
                if len(account) == 1 and account[0].account.deposit(total_value):
                    client = BrokerageClient.objects.get(id=request.session['brokerage_client_id'])
                    company,created = Company.objects.get_or_create(
                        symbol=quote['Symbol'],
                        name=quote['Name']
                    )
                    transaction = Transaction.objects.create(
                        company=company,
                        client=client,
                        quantity=-quantity,
                        share_price=int(quote['LastPrice'])
                    )
                    return render(request, self.template, {'transaction': transaction})
        return render(request, self.template)