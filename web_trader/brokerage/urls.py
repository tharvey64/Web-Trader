from django.conf.urls import patterns, include, url
from django.contrib import admin
from brokerage.views import IndexView,NewClientView,AccountView,BrokerView,ViewWithdraw,ViewDeposit

urlpatterns = patterns('',
    url(r'^$', IndexView.as_view(), name='home'),
    url(r'^new_client/', NewClientView.as_view(),name='new_client'),
    url(r'^account_view/', AccountView.as_view(),name='accounts_view'),
    url(r'^withdraw/', ViewWithdraw.as_view(),name='view'),
    url(r'^deposit/', ViewDeposit.as_view(),name='view'),
    # url(r'^transfer/', LogInView.as_view(),name='view'),
    url(r'^new_account/', BrokerView.as_view(),name='new_account'),
)
