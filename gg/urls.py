from django.conf.urls import patterns, include, url
from django.contrib.auth.views import login

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import logout


admin.autodiscover()
from foo.views import EntryView

import os
import settings


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'gg.views.home', name='home'),
    # url(r'^gg/', include('gg.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    (r'^log/', include('log_app.urls')),
    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    #(r'^comments/', include('django.contrib.comments.urls')),
    (r'^board/', include('foo.urls')),

    (r'accounts/login/', login),
    url(r'^account/$', login_required(generic.TemplateView.as_view(template_name='account_detail.html'))),
    (r'^accounts/logout/$', 'django.contrib.auth.views.logout',
        {'next_page': '/'}),
    url(r'^accounts/', include('registration_email.backends.simple.urls')),
    url(r'', include('social_auth.urls')),
    url(r'^$', (generic.TemplateView.as_view(template_name='index.html')), name="index"),
    #(r'^api/v2/', include('fiber.rest_api.urls')),
    #(r'^admin/fiber/', include('fiber.admin_urls')),
    (r'^i18n/', include('django.conf.urls.i18n')),
    (r'^jsi18n/$', 'django.views.i18n.javascript_catalog', {'packages': ('fiber',),}),
)

if os.environ.get('django_local', 0):
    urlpatterns += patterns('',
                            (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
                            (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
                            )


urlpatterns += patterns('',
                        url(r'^api-auth/', include('rest_framework.urls',
                                                   namespace='rest_framework')),
                        #(r'', 'fiber.views.page'),
                        )
