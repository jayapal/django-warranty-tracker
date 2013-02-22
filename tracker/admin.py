"""Admin for tracker application.

tracker/admin.py

Copyright 2013 Jayapal D
Jayapal D (jayapal.d@gmail.com)
"""
from django.contrib import admin
from django.forms import ModelForm

from tracker.models import *

class AdminProduct(admin.ModelAdmin):
    """ ModelAdmin for Product"""

    list_display = ['name', 'description', 'typ',
                    'expiry_date', 'notify_me', 'user']
    exclude = ['user']

    def queryset(self, request):
        # Return product list based on user
        qs = super(AdminProduct, self).queryset(request)
        if request.user.is_superuser:
            return qs
        else:
            return qs.filter(user=request.user)

    def save_model(self, request, obj, form, change):
        # save user object along with Product
        obj.user = request.user
        obj.save()

class AdminShop(admin.ModelAdmin):
    """ ModelAdmin for Shop """

    list_display = ['name', 'address']

class AdminProductType(admin.ModelAdmin):
    """ ModelAdmin for Product Type """

    list_display = ['name']


class AdminRemainder(admin.ModelAdmin):
    """ ModelAdmin for Remainder """

    list_display = ['days']
    fields = ['days']

    def queryset(self, request):
        # Need to show only requested user
        qs = super(AdminRemainder, self).queryset(request)
        if request.user.is_superuser:
            return qs
        else:
            return qs.filter(user=request.user)

# Register
admin.site.register(Product, AdminProduct)
admin.site.register(Shop, AdminShop)
admin.site.register(ProductType, AdminProductType)
admin.site.register(Remainder, AdminRemainder)
