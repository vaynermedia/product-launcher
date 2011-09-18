import ajax
from ajax.endpoints import ModelEndpoint
from ajax.encoders import encoder
from apps.rocket.models import Customer
from facebook import Facebook


class CustomerEndpoint(ModelEndpoint):
    def can_create(self, user, record):
        api = Facebook(added=True, api_key=settings.FACEBOOK_,
            app_id=, auth_token=, oauth2=True, oauth2_token=

    can_update = lambda self, user, record: False
    can_delete = can_update
    can_get = can_update


ajax.endpoint.register(Customer, CustomerEndpoint)
