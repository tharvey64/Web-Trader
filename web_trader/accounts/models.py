from django.db import models
import uuid
from users.models import User

# Create your models here.
# Find a way to default this on creation
# might want to hash the number
# Handle withdraw and deposit here
class Account(models.Model):
    number = models.CharField(max_length=17,unique=True)
    type_of = models.CharField(max_length=100, unique=True)
    balance = models.IntegerField()
    user = models.ForeignKey(User)

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

    def generate_account_number(self):
        self.number = uuid.uuid4()
        return self.number