from django.db import models
from users.models import User
from accounts.models import Account

# Create your models here.
class BrokerageClient(models.Model):
    user = models.ForeignKey(User)

class BrokerageAccount(models.Model):
    client = models.ForeignKey(BrokerageClient)
    account = models.ForeignKey(Account)