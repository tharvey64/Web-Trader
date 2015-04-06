from django.conf.urls import patterns, include, url
from django.contrib import admin
from bank.views import ViewAccount, ViewBanker, ViewIndex, ViewNewClient, ViewWithdraw, ViewDeposit, ViewTransfer

urlpatterns = patterns('',
    # Examples:
    # TEST
    url(r'^test/', 'bank.tests.test',name='test'),
    # ^^^TEST
    url(r'^$', ViewIndex.as_view(), name='home'),
    url(r'^new_client/', ViewNewClient.as_view(),name='new'),
	url(r'^view_account/', ViewAccount.as_view(),name='view'),
    url(r'^withdraw/', ViewWithdraw.as_view(),name='withdraw'),
    url(r'^deposit/', ViewDeposit.as_view(),name='deposit'),
    url(r'^banker/', ViewBanker.as_view(),name='banker'),
    url(r'^transfer/', ViewTransfer.as_view(),name='view'),
)
