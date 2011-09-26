from django.shortcuts import get_object_or_404
from django.shortcuts import render_to_response
from apps.rocket.models import Campaign
from apps.rocket.decorators import replace_with_models


@render_to('rocket/home.html')
def home(request):
    """The homepage for the product."""
    return {}


@replace_with_models
def campaign_home(request, campaign):
    """The landing page for a given campaign."""
    return render_to_response('campaigns/%s/home.html' % campaign.pk, {
        'campaign': campaign
    })


@replace_with_models
def campaign_step(request, campaign, step):
    return render_to_response('campaigns/%s/steps/%s.html' % step.pk, {
        'campaign': campaign,
        'step': step,
    })
