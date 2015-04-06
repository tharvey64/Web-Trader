from django.conf.urls import patterns, include, url
from django.contrib import admin
from stocks.views import IndexView

urlpatterns = patterns('',
    url(r'^$', IndexView.as_view(),name='index'),
    # url(r'^company_search/$', ),
    # url(r'^quote/$', ),
)