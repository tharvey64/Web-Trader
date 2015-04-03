from django.db import models

# Create your models here.
class Client(models.Model):
	balance = models.CharField(max_length=100)
	account_number = models.IntegerField()
	created_at = models.DateField(auto_now=True)
	updated_at = models.DateField(auto_now_add=True)