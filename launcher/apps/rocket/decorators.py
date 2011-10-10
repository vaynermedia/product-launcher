from django.http import Http404
from django.shortcuts import render_to_response
from decorator import decorator
from apps.rocket.models import RefererBlock
import re


@decorator
def replace_with_models(f, *args, **kwargs):
    for var, val in kwargs.iteritems():
        try:
            model_name = var[0].upper() + var[1:]
            module = __import__('launcher.apps.rocket.models', globals(),
                locals(), [model_name], -1)
            model = getattr(module, model_name)
            try:
                kwargs[var] = model.objects.get(pk=val)
            except model.DoesNotExist:
                kwargs[var] = False
        except (ImportError, AttributeError):
            pass

    return f(*args, **kwargs)


@decorator 
def gate_referers(f, *args, **kwargs):
    """Checks to make sure the person isn't coming from a gated site."""
    referer = request.META.get('HTTP_REFERER', '')
    for block in RefererBlock.objects.filter(campaign=args[1]):
        if re.search(block.pattern, referer):
            return render_to_response('campaigns/%s/gated.html' % campaign.pk,
                {'campaign': campaign})

    return f(*args, **kwargs)
