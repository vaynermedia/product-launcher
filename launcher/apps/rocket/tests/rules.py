from base import RocketTestCase
from apps.rocket.rules import BaseRule, MustHaveAgeRangeRule, \
    MustBeAdultRule, MustBeManRule, MustBeWomanRule
from apps.rocket.models import Session


class BaseRuleTests(RocketTestCase):
    def test_getattr(self):
        rule = BaseRule(Session(), foo='bar', baz=1)
        self.assertEquals('bar', rule.foo)
        self.assertEquals(1, rule.baz)
