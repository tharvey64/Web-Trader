from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^brokerage/', include('brokerage.urls'))
    url(r'^bank/', include('bank.urls'))
    url(r'^users/', include('users.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
