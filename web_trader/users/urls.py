from django.conf.urls import patterns, include, url
from django.contrib import admin
from users.views import MainView, LogInView, RegisterView, UserView

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'web_trader.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', MainView.as_view(),name='index'),
    url(r'^log_in/', LogInView.as_view(),name='log_in'),
    url(r'^register/', RegisterView.as_view(),name='register'),
    url(r'^home/', UserView.as_view(),name='home'),
)
