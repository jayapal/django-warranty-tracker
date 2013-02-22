"""
Call back function for tracker module

Copyright 2013 Jayapal D
Jayapal D (jayapal.d@gmail.com)
"""

from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.contrib.auth.models import Group
from django.contrib import messages

from tracker.forms import *
from tracker.models import Remainder

# Render SignUp page
def signup(request):
    if request.user.is_authenticated():
        # Redirect to profile page, if user is already logged in
        return HttpResponseRedirect('/')

    template = 'tracker/registration/signup.html'
    if request.method == 'POST':
        # Passing the form data to Signupform
        form = SignupForm(request.POST)
        if form.is_valid():
            # Valid form and create user
            user = User.objects.create_user(form.data['username'],
                                            form.data['email'],
                                            form.data['password'])
            # Add extra attribute of users
            user.first_name = form.data['first_name']
            user.last_name = form.data['last_name']
            user.is_staff = True # grant permission to access admin site
            user.save() # save user details all together

            # Add user in default group and enable permission
            g = Group.objects.get(name='User') 
            g.user_set.add(user)

            # Add default Remainder days settings
            r = Remainder(user=user)
            r.save()

            # redirect to login page
            msg = ('Successfully created account for %s. Please login.')\
                  %(user.get_full_name())
            messages.info(request, msg)
            return HttpResponseRedirect('/')
    else:
        # Create empty signup form
        form = SignupForm()
    return render_to_response(template, {'form': form},
                              context_instance=RequestContext(request))
