from base import RocketTestCase
from apps.rocket.models import Decision, Customer, Session


class DecisionTests(RocketTestCase):
    def setUp(self):
        self.decision = Decision()
        self.decision.rules = 'MustBeAdult|MustBeMan|MustHaveAgeRange' + \
            '?range=18,44'

        self.customer = Customer()
        self.customer.first_name = 'Joe'
        self.customer.last_name = 'Joe'
        self.customer.email = 'joe@joestump.net'
        self.customer.uid = 999999999
        self.customer.gender = 'M'
        self.customer.age = 31
        self.customer.access_token = 'a0s98df70as897df098a7g'
        self.customer.timezone = -8

        self.session = Session()
        self.session.customer = self.customer

    def test_parse_rules(self):
        rules = self.decision.parse_rules()

        expected_rules = ['MustBeAdult', 'MustBeMan', 'MustHaveAgeRange']
        actual_rules = [r['rule'] for r in rules]
        actual_rules.sort()

        self.assertEquals(expected_rules, actual_rules)

        expected_args = [{}, {}, {'range': ['18', '44']}]
        actual_args = [r['args'] for r in rules]
        actual_args.sort()

        self.assertEquals(expected_args, actual_args)

    def test_inquire(self):
        self.assertTrue(self.decision.inquire(self.session))  
