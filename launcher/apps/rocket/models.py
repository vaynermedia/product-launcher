from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from apps.rocket import rules
from django_extensions.db.fields.json import JSONField
from django.template.loader import render_to_string


class Client(models.Model):
    name = models.CharField(max_length=100)

    def __unicode__(self):
        return self.name


class Brand(models.Model):
    name = models.CharField(max_length=100)
    client = models.ForeignKey('Client')

    def __unicode__(self):
        return self.name


class Campaign(models.Model):
    brand = models.ForeignKey('Brand', related_name='campaigns',
        blank=True, null=True, default=None)
    begins = models.DateTimeField()
    ends = models.DateTimeField()    
    active = models.BooleanField()
    total_units = models.PositiveIntegerField(default=0)
    google_analytics_code = models.CharField(max_length=100, default='')

    @property
    def facebook_app_id(self):
        return settings.FACEBOOK_APP_ID

    def next_step(self, session):
        if session.last_step:
            for step in Step.objects.filter(campaign=self,
                sort__gt=session.last_step.sort).order_by('sort'):
                for decision in Decision.objects.filter(step=step):
                    if decision.inquire(session):
                        return step
        else:
            # If there is no last step, return the first step, which has no
            # decisions attached to it.
            return Step.objects.filter(campaign=self).order_by('sort')[0]


class RefererBlock(models.Model):
    campaign = models.ForeignKey('Campaign')
    pattern = models.CharField(max_length=100)


class Step(models.Model):
    name = models.CharField(max_length=100)
    sort = models.PositiveIntegerField()
    campaign = models.ForeignKey('Campaign', related_name='steps')
    templates = models.CharField(max_length=100, blank=True, null=True)

    def render(self, session):
        pass

class Decision(models.Model):
    class Rejected(Exception):
        pass

    step = models.ForeignKey('Step', related_name='decisions')
    rules = models.CharField(max_length=100, default='')
    goto = models.ForeignKey('Step')
    match_all = models.BooleanField(default=True)
    sort = models.PositiveIntegerField(default=0)

    def parse_rules(self):
        parts = self.rules.strip().split('|')
        rules = []
        for p in parts:
            args = {}
            if '?' in p:
                rule, args_string = p.split('?')
                if args_string:
                    for a in args_string.split('&'):
                        var, val = a.split('=')
                        if ',' in val:
                            val = val.split(',') 

                        args[var] = val
            else:
                rule = p.strip()

            rules.append({
                'rule': rule,
                'args': args
            })

        return rules

    def inquire(self, session):
        rules_matched = 0
        parsed_rules = self.parse_rules()
        for r in parsed_rules:
            try:
                cls = getattr(rules, r['rule'])
            except AttributeError:
                continue # Ignore invalid rules for now.
        
            rule = cls(session, **r['args'])
            if not rule.match():
                rules_matched += 1 
 
        # Check to see if we're a decision requiring all rules to be matched
        # or if none of the rules matched up.
        if (self.match_all and rules_matched != len(parsed_rules)) or \
            rules_matched == 0:
            raise Decision.Rejected()
        
        return True


class Customer(models.Model):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('U', 'Unknown'),
    )

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(db_index=True)
    uid = models.PositiveIntegerField(db_index=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES,
        db_index=True, default='U')
    age = models.PositiveIntegerField(default=0)
    access_token = models.CharField(max_length=255)
    campaign = models.ForeignKey('Campaign')
    timezone = models.IntegerField(default=0)
    meta = JSONField()


class Session(models.Model):
    campaign = models.ForeignKey('Campaign', blank=True, null=True)
    customer = models.ForeignKey('Customer', blank=True, null=True)
    last_step = models.ForeignKey('Step', blank=True, null=True, default=None)
