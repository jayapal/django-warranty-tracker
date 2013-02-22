Readme for Django warranty tracker
Copyright 2013 Jayapal D
Jayapal D (jayapal.d@gmail.com)
-------------------------------

Django Warranty Tracker
-----------------------

Application is used to keep remainder for warranty expire date of a product.
Email will be received to user about when they are expiring and which are already expired.

Use Case
-------------

1. Create a new account using django default admin site.
2. After creating accout, you can login to the application.
3. By default, your email remainder days settings will be configured as 7 days,
   If needed, you can change it from the dashboard.
4. Now add the products and it attributes.
5. Now you will be receiving emails based on reamainder days settings.
6. Email will have "when they are expiring and which are already expired".


Deployment
-----------

1. Get the latest code from github
2. Configure DB settings in settings.py
3. Configure Email settings in settings.py
4. python manage.py syncdb (for first time)
5. python manage.py migrate
6. python manage.py runserver
7. set cron tab for the command "python manage.py email_notification" 
8. Now you can play around the application.


Internal Process
----------------

1. When you do the syndb first time, a new group "User" will be create with 
   defult permission. You can look in to the file "tracker/management/__init__.py"

2. When user create a new profile, we are adding the user in default group "User".

Support & Bug
-------------

Please contact me at jayapal.d@gmail.com
