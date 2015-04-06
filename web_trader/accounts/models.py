import uuid
from django.db import models

class Account(models.Model):
    number = models.CharField(max_length=17,unique=True,default=None)
    balance = models.DecimalField(max_digits=12,decimal_places=2,default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def withdraw(self, amount):
        if amount > self.balance:
            return False
        self.balance -= amount
        self.save()
        return True

    def deposit(self, amount):
        if amount < 0:
            return False
        self.balance += amount
        self.save()
        return True

    def _account_number(self):
        new_number = ''
        while not new_number:
            new_number = str(uuid.uuid4().int)[:17]
            if Account.objects.filter(number=new_number):
                new_number = ''
        return new_number

    def save(self,*arg,**kwargs):
        if not self.number:
            self.number = self._account_number()
        super().save(*arg,**kwargs)
