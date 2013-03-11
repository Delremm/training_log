from django.conf.urls import patterns, include, url
from django.contrib.auth.views import login

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()
from foo.views import EntryView
from log.views import TestView

import settings
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'gg.views.home', name='home'),
    # url(r'^gg/', include('gg.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    (r'^comments/', include('django.contrib.comments.urls')),
    (r'^board/', include('foo.urls')),
    (r'^', include('log.urls')),
    (r'^log/', include('log_app.urls')),
    (r'accounts/login/', login),
     (r'^test/$', TestView.as_view()),
    (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
    (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
)

urlpatterns += patterns('',
                        url(r'^api-auth/', include('rest_framework.urls',
                                                   namespace='rest_framework')),
                        )
