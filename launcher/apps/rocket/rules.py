class BaseRule(object):
    def __init__(self, session, **kwargs):
        self.session = session

        if not self.session.customer:
            raise ValueError('Sessions must have customers.')

        self.arguments = kwargs

    def __getattr__(self, name):
        try:
            return self.arguments[name]
        except KeyError:
            raise AttributeError()


class MustHaveAgeRangeRule(BaseRule):
    def match(self):
        if self.session.customer.age >= self.range[0] and \
            self.session.customer.age <= self.range[1]:
            return True

        return False


class MustBeAdultRule(BaseRule):
    def match(self):
        if self.session.customer.age >= 18:
            return True
        
        return False


class MustBeManRule(BaseRule):
    def match(self):
        if self.session.customer.gender == 'M':
            return True

        return False


class MustBeWomanRule(BaseRule):
    def match(self):
        if self.session.customer.gender == 'F':
            return True

        return False
