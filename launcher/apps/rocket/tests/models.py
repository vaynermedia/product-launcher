from base import RocketTestCase
from apps.rocket.models import Decision


class DecisionTests(RocketTestCase):
    def test_parse_rules(self):
        d = Decision()
        d.rules = 'MustBeAdult|MustBeMan|MustHaveAgeRange?range=18,24'
        rules = d.parse_rules()

        expected_rules = ['MustBeAdult', 'MustBeMan', 'MustHaveAgeRange']
        actual_rules = [r['rule'] for r in rules]
        actual_rules.sort()

        self.assertEquals(expected_rules, actual_rules)

        expected_args = [{}, {}, {'range': ['18', '24']}]
        actual_args = [r['args'] for r in rules]
        actual_args.sort()

        self.assertEquals(expected_args, actual_args)
