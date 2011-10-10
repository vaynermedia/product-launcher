from django.shortcuts import get_object_or_404, render_to_response
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from apps.rocket.models import Campaign
from apps.rocket.decorators import replace_with_models, gate_referers
import random


@render_to('rocket/home.html')
def home(request):
    """The homepage for the product."""
    return {}


@replace_with_models
@gate_referers
def campaign_home(request, campaign):
    """The landing page for a given campaign."""
    session = get_session(request, campaign)
    if session:
        # This person has been here before so redirect them. This is only
        # session based. They can re-authenticate, but the AJAX endpoint
        # will find their old session and route them accordingly.
        return HttpResponseRedirect(reverse('rocket_campaign_route',
            args=[campaign.pk]))

    return render_to_response('campaigns/%s/home.html' % campaign.pk, {
        'campaign': campaign
    })


@replace_with_models
@gate_referers
def campaign_route(request, campaign):
    """This routes people after every successful step."""
    session = get_session(request, campaign)
    if not session:
        # If they have no session and are attempting to route themselves,
        # route them back to the home. 
        return HttpResponseRedirect(reverse('rocket_campaign_home',
            args=[campaign.pk]))

    step = campaign.next_step(session)
    return HttpResponseRedirect(reverse('rocket_campaign_step',
        args=[campaign.pk, step.pk]))


@replace_with_models
def campaign_sorry(request, campaign):
    """Users are sent here who are not allowed to redeem."""
    return render_to_response('campaigns/%s/sorry.html' % campaign.pk, {
        'campaign': campaign
    })


@replace_with_models
@gate_referers
def campaign_step(request, campaign, step):
    if step.templates:
        templates = [t.strip() for t in step.templates.split(',')]
        template_name = random.choice(templates)
    else:
        template_name = '%s' % step.pk

    return render_to_response('campaigns/%s/steps/%s.html' % template_name, {
        'campaign': campaign,
        'step': step,
    })
