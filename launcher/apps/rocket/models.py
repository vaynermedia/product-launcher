from django.db import models


class Client(models.Model):
    name = models.CharField(max_length=100)


class Product(models.Model):
    name = models.CharField(max_length=100)


class Campaign(models.Model):
    product = models.ForeignKey('Product')
    begins = models.DateTimeField()
    ends = models.DateTimeField()    


class Customer(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    uid = models.PositiveIntegerField()
