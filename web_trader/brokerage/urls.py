from django.conf.urls import patterns, include, url
from django.contrib import admin
import brokerage.views as view

urlpatterns = patterns('',
    url(r'^$', view.IndexView.as_view(), name='home'),
    url(r'^new_client/', view.NewClientView.as_view(), name='new_client'),
    url(r'^portfolio_menu/', view.PortfolioMenuView.as_view(), name='portfolio_menu'),
    url(r'^portfolio/', view.PortfolioView.as_view(), name='portfolio'),
    url(r'^purchase_stock/', view.PurchaseView.as_view(), name='purchase'),
    url(r'^sell_stock', view.SellView.as_view(), name='sell'),
    url(r'^account_menu/', view.AccountMenuView.as_view(), name='account_menu'),
    url(r'^account_view/', view.AccountView.as_view(), name='accounts_view'),
    url(r'^withdraw/', view.WithdrawView.as_view(),name='withdraw'),
    url(r'^deposit/', view.DepositView.as_view(),name='deposit'),
    url(r'^transfer/', view.TransferView.as_view(), name='transfer'),
    url(r'^new_account/', view.BrokerView.as_view(), name='new_account'),
)
