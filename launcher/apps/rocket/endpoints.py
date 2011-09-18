from django.conf import settings
import ajax
import facebook
from ajax.endpoints import ModelEndpoint
from ajax.encoders import encoder
from apps.rocket.models import Customer
from django.utils import simplejson as json


class CustomerEndpoint(ModelEndpoint):
    def can_create(self, user, record):
        return True

    def authenticate(self, request, application, method):
        graph = facebook.GraphAPI(request.POST['access_token'])
        try:
            data = graph.get_object(request.POST['uid'])
        except Exception, e:
            return False

        if int(data['id']) == int(request.POST['uid']):
            return True
        else:
            return False

    can_update = lambda self, user, record: False
    can_delete = can_update
    can_get = can_update


ajax.endpoint.register(Customer, CustomerEndpoint)
