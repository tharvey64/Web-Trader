from django.conf.urls import patterns, include, url
from django.contrib import admin
from brokerage.views import IndexView,NewClientView,AccountView,BrokerView,PortfolioMenuView,AccountMenuView
from brokerage.views import PortfolioView,PurchaseView,SellView,WithdrawView,DepositView

urlpatterns = patterns('',
    url(r'^$', IndexView.as_view(), name='home'),
    url(r'^new_client/', NewClientView.as_view(), name='new_client'),
    url(r'^portfolio_menu/', PortfolioMenuView.as_view(), name='portfolio_menu'),
    url(r'^portfolio/',PortfolioView.as_view(), name='portfolio'),
    url(r'^purchase_stock/', PurchaseView.as_view(), name='purchase'),
    url(r'^sell_stock',SellView.as_view(), name='sell'),
    url(r'^account_menu/', AccountMenuView.as_view(), name='account_menu'),
    url(r'^account_view/', AccountView.as_view(), name='accounts_view'),
    url(r'^withdraw/', WithdrawView.as_view(),name='withdraw'),
    url(r'^deposit/', DepositView.as_view(),name='deposit'),
    # url(r'^transfer/', LogInView.as_view(), name='view'),
    url(r'^new_account/', BrokerView.as_view(), name='new_account'),
)
