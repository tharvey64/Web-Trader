from django.db import models
from users.models import User
from accounts.models import Account

# Create your models here.

class Bank(models.Model):
	class BankClient(models.Model):
   		user = models.ForeignKey(User)

	class BankAccount(models.Model):
    	client = models.ForeignKey(BankClient)
    	account = models.ForeignKey(Account)