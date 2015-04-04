from django.conf.urls import patterns, include, url
from django.contrib import admin
from users.views import MainView, LogInView, RegisterView

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'web_trader.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', MainView.as_view(),name='index'),
)
