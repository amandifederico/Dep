from django.conf.urls import patterns, include, url
#
from django.conf.urls.defaults import * 
from django.contrib.auth.views import login, logout
#
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from depoapp.views import *
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'depo.views.home', name='home'),
    # url(r'^depo/', include('depo.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    (r'^listado/$',listado),
    (r'^accounts/login/$', 'django.contrib.auth.views.login'),
    (r'^site_media/(?P<path>.*)$','django.views.static.serve',
        {'document_root': '/var/www/depo/media'}),
    (r'^static/(?P<path>.*)$','django.views.static.serve',
        {'document_root': '/var/www/depo/media'}),
)
