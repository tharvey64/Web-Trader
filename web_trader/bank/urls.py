from django.conf.urls import patterns, include, url
from django.contrib import admin
import bank.views as view

urlpatterns = patterns('',
    # Examples:
    url(r'^$', view.IndexView.as_view(), name='home'),
    url(r'^new_client/', view.NewClientView.as_view(),name='new'),
	url(r'^view_account/', view.AccountView.as_view(),name='view'),
    url(r'^withdraw/', view.WithdrawView.as_view(),name='withdraw'),
    url(r'^deposit/', view.DepositView.as_view(),name='deposit'),
    url(r'^banker/', view.BankerView.as_view(),name='banker'),
    url(r'^transfer/', view.TransferView.as_view(),name='view'),
)
