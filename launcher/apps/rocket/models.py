from django.db import models


class Client(models.Model):
    name = models.CharField(max_length=100)
    total_units = models.PositiveIntegerField(default=0)


class Product(models.Model):
    name = models.CharField(max_length=100)


class Campaign(models.Model):
    product = models.ForeignKey('Product', related_name='campaigns')
    begins = models.DateTimeField()
    ends = models.DateTimeField()    


class RefererBlock(models.Model):
    campaign = models.ForeignKey('Campaign')
    match = models.CharField(max_length=100)


class Step(models.Model):
    name = models.CharField(max_length=100)
    sort = models.PositiveIntegerField()
    campaign = models.ForeignKey('Campaign', related_name='steps')

    def next(self):
        pass


class Decision(models.Model):
    step = models.ForeignKey('Step', related_name='decisions')
    rules = models.CharField(max_length=100, default='')
    goto = models.ForeignKey('Step')
    match_all = models.BooleanField(default=True)

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


class Session(models.Model):
    customer = models.ForeignKey('Customer', blank=True, null=True) 
