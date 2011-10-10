from apps.rocket.models import Session

def get_session(request, campaign):
    pk = request.session.get('campaign_%s' % campaign.pk, None)
    if not pk:
        return None

    return Session.objects.get(pk
