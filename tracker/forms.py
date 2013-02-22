"""
forms for tracker module

Copyright 2013 Jayapal D
Jayapal D (jayapal.d@gmail.com)
"""

from django import forms
from django.contrib.auth.models import User

# Username field for signup form
class UserField(forms.CharField):
    def clean(self, value):
        super(UserField, self).clean(value)
        try:
            # check for username availability
            User.objects.get(username=value)
            raise forms.ValidationError("Someone is already using this"
                                        "username. Please pick an other.")
        except User.DoesNotExist:
            return value


# Signup form
class SignupForm(forms.Form):
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    username = UserField(max_length=30)
    email = forms.EmailField()
    email2 = forms.EmailField(label="Repeat your email")
    password = forms.CharField(widget=forms.PasswordInput())
    password2 = forms.CharField(widget=forms.PasswordInput(), label="Repeat your password")

    
    def clean_email(self):
        # Validate email address
        if self.data['email'] != self.data['email2']:
            raise forms.ValidationError('Emails are not the same')
        return self.data['email']

    def clean_password(self):
        # Validate password
        if self.data['password'] != self.data['password2']:
            raise forms.ValidationError('Passwords are not the same')
        return self.data['password']

    def check_email_exist(self):
        # Check for email availability
        try:
            User.objects.get(email=self.data['email'])
            raise forms.ValidationError("Email already registered.")
        except User.DoesNotExist:
            pass
    
    def clean(self,*args, **kwargs):
        self.clean_email()
        self.check_email_exist()
        self.clean_password()
        return super(SignupForm, self).clean(*args, **kwargs)
