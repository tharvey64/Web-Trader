import requests
from django.db import models

# Create your models here.
class Company(models.Model):
    symbol = models.CharField(max_length=15)
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Markit:
    company_search_url = 'http://dev.markitondemand.com/Api/v2/Lookup/json?input='
    quote_url = 'http://dev.markitondemand.com/Api/v2/Quote/json?symbol='

    @classmethod
    def find_company(cls, name):
        if not isinstance(name, str):
            return [{'Message':'Error: Invalid Input Type'}]
        r = requests.get(cls.company_search_url + name).json()
        return r

    @classmethod
    def find_quote(cls, symbol):
        if not isinstance(symbol, str):
            return {'Message':'Error: Invalid Input Type'}
        r = requests.get(cls.quote_url + symbol).json()
        return r

    # http://finance.yahoo.com/q?s=APPL&ql=1
    # might become static method
    # @classmethod
    # def market_view(cls):

    # @classmethod
    # def market_news(cls,**kwargs):
        
    # @classmethod
    # def security_news(cls,**kwargs):


