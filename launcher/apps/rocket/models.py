from django.db import models


class Client(models.Model):
    name = models.CharField(max_length=100)


class Product(models.Model):
    name = models.CharField(max_length=100)


class Campaign(models.Model):
    product = models.ForeignKey('Product', related_name='campaigns')
    begins = models.DateTimeField()
    ends = models.DateTimeField()    


class Step(models.Model):
    name = models.CharField(max_length=100)
    sort = models.PositiveIntegerField()
    campaign = models.ForeignKey('Campaign', related_name='steps')


class Rule(models.Model):
    BEHAVIOR_CHOICES = (
        ('MustBeAdultRule', 'Must be Adult'),
        ('MustBeManRule', 'Must be a Man'),
        ('MustBeWomanRule', 'Must be a Woman'),
    )

    name = models.CharField(max_length=100)
    behavior = models.CharField(max_length=10, choices=BEHAVIOR_CHOICES)
    active = models.BooleanField(default=True)


class Decision(models.Model):
    step = models.ForeignKey('Step', related_name='decisions')
    rule = models.ForeignKey('Rule')
    goto = models.ForeignKey('Step')
    match_all = models.BooleanField(default=True)


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
