"""
Modle for tracker module

Copyright 2013 Jayapal D
Jayapal D (jayapal.d@gmail.com)
"""
from django.db import models
from django.contrib.auth.models import User

# Define the type of product
class ProductType(models.Model):
    name = models.CharField(max_length=255)

    def __unicode__(self):
        return self.name

# Define the shop details
class Shop(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)

    def __unicode__(self):
        return self.name

# List of products
class Product(models.Model):
    user = models.ForeignKey(User)
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255, blank=True, null=True)
    typ = models.ForeignKey(ProductType)
    purchase_date = models.DateField()    
    manufacture_date = models.DateField()
    expiry_date = models.DateField()
    bill_no = models.CharField(max_length=100, blank=True, null=True)
    price = models.IntegerField()
    shop = models.ForeignKey(Shop, blank=True, null=True)
    notify_me = models.BooleanField(default=True)

    def __unicode__(self):
        return self.name

# Define the type of product
class Remainder(models.Model):
    user = models.ForeignKey(User, unique=True)
    days = models.CharField(max_length=2, default=7,
                            verbose_name="Remainder notification days settings.")

    def __unicode__(self):
        return self.days

