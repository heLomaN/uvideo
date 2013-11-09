from django.conf.urls import patterns, include, url

from uvideo.views import about_us

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'uvideo.views.home', name='home'),
    url(r'^play/', include('play.urls')),
    url(r'^about-us/', about_us),
    url(r'^$', about_us),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
