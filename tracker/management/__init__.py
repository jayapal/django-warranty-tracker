"""
Create Default group and add permission

Copyright 2013 Jayapal D
Jayapal D (jayapal.d@gmail.com)
"""

from django.db.models.signals import post_syncdb
from django.contrib.auth.models import Group, Permission
import tracker.models

def create_group_with_permission(sender, **kwargs):
    # List of permission which
    perms = ['Can add product',
             'Can change product',
             'Can delete product',
             'Can change remainder',
             'Can add shop',
             'Can add product type',
            ]
    # Create default group
    print "Create default group User"
    g, created = Group.objects.get_or_create(name='User')
    # Adding permission for the group
    print "Granting permission to group User"
    for p in perms:
        permission = Permission.objects.get(name=p)
        g.permissions.add(permission)

# Signal
post_syncdb.connect(create_group_with_permission, tracker.models)
