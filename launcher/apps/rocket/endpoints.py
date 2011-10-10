from django.conf import settings
import ajax
import facebook
from ajax.endpoints import ModelEndpoint
from ajax.encoders import encoder
from ajax.exceptions import AJAXError
from apps.rocket.models import Customer, Campaign
from django.utils import simplejson as json


class CreateCustomer(object):
    def new_customer(self, campaign, data):
        customer = Customer()
        customer.first_name = data['first_name']
        customer.last_name = data['last_name']
        customer.email = data['email']
        customer.uid = int(data['uid'])
        customer.gender = data['gender']
        customer.age = int(data['age'])
        customer.access_token = data['access_token']
        customer.campaign = campaign
        customer.timezone = int(data['timezone'])
        customer.meta = data['meta']
        customer.save()
        return customer

    def check_access_token(self, data):
        graph = facebook.GraphAPI(data['access_token'])
        try:
            result = graph.get_object(data['uid'])
        except Exception, e:
            raise Exception('Invalid Facebook uid provided.')

        if int(result['id']) == int(data['uid']):
            raise Exception('Mismatched values for Facebook uid provided.')

    def __call__(self, request):
        self.check_access_token(request.POST)

        try:
            campaign = Campaign.objects.get(pk=int(request.POST['campaign']))
        except (KeyError, Campaign.DoesNotExist):
            raise AJAXError(404, "Invalid or unknown campaign.")

        try:
            customer = Customer.objects.get(uid=int(request.POST['uid']))
            if customer.access_token != request.POST['access_token']:
                customer.access_token = request.POST['access_token']
                customer.save()
        except:
            customer = self.new_customer(campaign, request.POST)

        session_key = 'campaign_%s' % campaign.pk
        try:
            pk = request.session.get(session_key)
            session = Session.objects.get(pk=session)
        except KeyError:
            try:
                session = Session.objects.get(campaign=campaign,
                    customer=customer)
            except Session.DoesNotExist:
                sesssion = Session()
                session.customer = customer
                session.campaign = campaign
                session.save()

        request.session[session_key] = session.pk

        return {
            'customer': customer.pk,
            'session': session.pk,
        }


create_customer = CreateCustomer()
