from django.conf.urls.defaults import patterns, include, url
from django.conf import settings
from django.contrib import admin


admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'launcher.apps.rocket.views.home', name='home'),
    url(r'^rocket/', include('launcher.apps.rocket.urls')),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^(static|media)/(?P<path>.*)$', 'django.views.static.serve',
            {'document_root': '../html/static'}),
    )
