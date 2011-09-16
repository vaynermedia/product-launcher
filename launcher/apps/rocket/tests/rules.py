from base import RocketTestCase
from apps.rocket.rules import BaseRule, MustHaveAgeRangeRule, \
    MustBeAdultRule, MustBeManRule, MustBeWomanRule
from apps.rocket.models import Session, Customer

class RulesTestCase(RocketTestCase):
    def setUp(self):
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


class BaseRuleTests(RulesTestCase):
    def test_getattr(self):
        rule = BaseRule(self.session, foo='bar', baz=1)
        self.assertEquals('bar', rule.foo)
        self.assertEquals(1, rule.baz)

    def test_no_customer_raises_exception(self):
        func = lambda: BaseRule(Session())
        self.assertRaises(ValueError, func)


class MustBeAdultRuleTests(RulesTestCase):
    def test_exactly_18_is_adult(self):
        """Make sure someone exactly 18 is considered an adult."""
        self.session.customer.age = 18
        rule = MustBeAdultRule(self.session)
        self.assertTrue(rule.match())

    def test_over_18_is_adult(self):
        """Make sure someone over 18 is considered an adult."""
        rule = MustBeAdultRule(self.session)
        self.assertTrue(rule.match())

    def test_under_18_is_rejected(self):
        """Make sure someone under 18 is NOT considered an adult."""
        self.session.customer.age = 13
        rule = MustBeAdultRule(self.session)
        self.assertFalse(rule.match())

class MustHaveAgeRangeRuleTests(RulesTestCase):
    def test_age_in_range_is_accepted(self):
        """Make sure an age that falls in the range is valid."""
        rule = MustHaveAgeRangeRule(self.session, range=[18, 35])
        self.assertTrue(rule.match())

    def test_age_not_in_range_is_denied(self):
        """Make sure an age that falls outside of range is invalid."""
        rule = MustHaveAgeRangeRule(self.session, range=[60, 70])
        self.assertFalse(rule.match())

class MustBeManRuleTests(RulesTestCase):
    def test_males_are_accepted(self):
        """Make sure males are accepted."""
        rule = MustBeManRule(self.session)
        self.assertTrue(rule.match())

    def test_females_are_denied(self):
        """Make sure females are not accepted as males."""
        self.session.customer.gender = 'F'
        rule = MustBeManRule(self.session)
        self.assertFalse(rule.match())

class MustBeWomanRuleTests(RulesTestCase):
    def test_females_are_accepted(self):
        """Make sure females are accepted."""
        self.session.customer.gender = 'F'
        rule = MustBeWomanRule(self.session)
        self.assertTrue(rule.match())

    def test_males_are_denied(self):
        rule = MustBeWomanRule(self.session)
        self.assertFalse(rule.match())
