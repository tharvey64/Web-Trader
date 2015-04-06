from django.conf.urls import patterns, include, url
from django.contrib import admin
from stocks.views import IndexView, CompanySearchView, QuoteView

urlpatterns = patterns('',
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^company_search/$', CompanySearchView.as_view(), name='search'),
    url(r'^quote/$', QuoteView.as_view(), name='quote'),
)