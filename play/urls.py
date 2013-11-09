from django.conf.urls import patterns, include, url

from play.views import index,play

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'uvideo.views.home', name='home'),
    
    url(r'^index/$', index),
    url(r'^(?P<play_id>\d+)/$', play),
)
