from django.db import models
from users.models import User
from accounts.models import Account
from stocks.models import Company

# Create your models here.
class BrokerageClient(models.Model):
    user = models.ForeignKey(User)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class BrokerageAccount(models.Model):
    client = models.ForeignKey(BrokerageClient)
    account = models.ForeignKey(Account)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Transaction(models.Model):
    company = models.ForeignKey(Company)
    client = models.ForeignKey(BrokerageClient)
    quantity = models.IntegerField()
    unit_price = models.DecimalField(max_digits=12,decimal_places=3)
    created_at = models.DateTimeField(auto_now_add=True)