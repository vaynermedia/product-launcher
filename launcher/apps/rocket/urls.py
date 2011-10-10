from django.conf.urls.defaults import patterns, url
from django.views.generic.simple import redirect_to


urlpatterns = patterns('launcher.apps.rocket.views',
    url(r'^/?$', redirect_to, {'url': '/'}),
    url(r'^campaign/(?P<campaign>\d+)/?$', 'campaign_home',
        name='rocket_campaign_home'),
    url(r'^campaign/(?P<campaign>\d+)/(?P<step>\d+)/?$', 'campaign_step',
        name='rocket_campaign_step'),
    url(r'^campaign/(?P<campaign>\d+)/route/?$', 'campaign_route',
        name='rocket_campaign_route'),
)
