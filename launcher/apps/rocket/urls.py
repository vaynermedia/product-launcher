from django.conf.urls.defaults import patterns, url
from django.views.generic.simple import redirect_to


urlpatterns = patterns('launcher.apps.rocket.views',
    url(r'^/?$', redirect_to, {'url': '/'}),
)
