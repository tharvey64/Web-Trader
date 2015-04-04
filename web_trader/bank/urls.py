from django.conf.urls import patterns, include, url
from django.contrib import admin
from users.views import MainView, RegisterView

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'web_trader.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^view_account/', LogInView.as_view(),name='view'),
    url(r'^withdraw/', LogInView.as_view(),name='view'),
    url(r'^deposit/', LogInView.as_view(),name='view'),
    url(r'^transfer/', LogInView.as_view(),name='view'),
    url(r'^banker/', LogInView.as_view(),name='view'),
)
