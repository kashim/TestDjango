from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'TestDjango.views.home', name='home'),
    # url(r'^TestDjango/', include('TestDjango.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^poll/$', 'poll.views.index'),
    url(r'^poll/(?P<poll_id>\d+)/$', 'poll.views.detail'),
    url(r'^poll/(?P<poll_id>\d+)/results/$', 'poll.views.results'),
    url(r'^poll/(?P<poll_id>\d+)/vote/$', 'poll.views.vote'),     
)
