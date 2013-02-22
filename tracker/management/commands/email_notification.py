"""
Custom Command for sending email for user

Usage: ./manage.py email_notification

Please set this commands in cron tab for automating 

Copyright 2013 Jayapal D
Jayapal D (jayapal.d@gmail.com)
"""

from datetime import datetime, timedelta
import thread
import time

from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import User
from django.conf import settings
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives

from tracker.models import Product, Remainder

# Get the configured remainder days settings
def get_remainder_days(user):
    try:
        return int(Remainder.objects.get(user=user).days)
    except:
        return 2 # default 7 days

# Send email to user 
def send_email_notification(user, products):
    # context dict
    user_name = user.get_full_name() if user.get_full_name() else user.username
    ctx_dict = {'user_name': user_name, 'products': products, 'now': datetime.now().date()}

    # Get the subject
    subject = render_to_string('tracker/email/notification_subject.txt')
    subject = ''.join(subject.splitlines())

    # Get the email content
    message = render_to_string('tracker/email/'
                               'notification_email_content.txt',
                               ctx_dict)

    # Create Email instance
    msg = EmailMultiAlternatives(subject, message,
                                 settings.DEFAULT_FROM_EMAIL, [user.email])
    # Define message has html content
    msg.attach_alternative(message, "text/html")
    msg.send() # send email

class Command(BaseCommand):
    help = 'Send email notification to user'

    def handle(self, *args, **options):
            now = datetime.now()
            # Get the users list
            for u in User.objects.filter(is_active=True):
                # Calculate the remainder days
                date_to_add = timedelta(days=get_remainder_days(u))
                earlier_date = now + date_to_add
                # Fetch all the products with in the remainder time period
                products = Product.objects.filter(notify_me=True,
                               expiry_date__lte=earlier_date).order_by('expiry_date')
                # Send email
                try:
                    send_email_notification(u, products)
                except Exception, e:
                    self.stdout.write(str(e))                 
            self.stdout.write('Email sent successfully.')
