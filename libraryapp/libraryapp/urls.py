from django.conf.urls import patterns, include, url
from libapp.views import *
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^libapp/', include('libapp.urls')),
    url(r'^accounts/login/$', LoginRequest, name='login'),
	url(r'^accounts/logout/$', LogoutRequest, name='LogoutRequest'),
    #url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
