import ajax
from ajax.endpoints import ModelEndpoint
from ajax.encoders import encoder
from apps.rocket.models import Customer


class CustomerEndpoint(ModelEndpoint):
    def can_create(self, user, record):
        return True

    can_update = lambda self, user, record: False
    can_delete = can_update
    can_get = can_update


ajax.endpoint.register(Customer, CustomerEndpoint)
