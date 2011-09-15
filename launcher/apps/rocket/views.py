from django.shortcuts import get_object_or_404
from sugar.views.decorators import render_to
from apps.rocket.models import Campaign
from apps.rocket.decorators import replace_with_models


@render_to('rocket/home.html')
def home(request):
    """The homepage for the product."""
    return {}


@replace_with_models
@render_to('rocket/campaign/home.html')
def campaign_home(request, campaign):
    """The landing page for a given campaign."""
    return {
        'campaign': campaign
    }
