"""Utility functions used by multiple AVA apps.

Be careful not to import too many AVA modules here, as that could
create a recipe for annoying circular dependencies. It's fine to
import Django stuff or system libraries as needed.
"""
# Django Imports
from django.conf import settings
import django.contrib.auth.decorators
# Email Imports
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
# Python Imports
import smtplib


def is_ava_superuser(user):
    """True if the user is an AVA superuser.

    That is: they have the UserRights.is_admin attribute *and*
    the Django user.is_superuser.attribute.
    """
    return user.is_superuser and user.rights.is_admin


# Create a simple decorator that can be used to ensure
# a user is an AVA superuser before accessing a view.
# Based on user_passes_test.
#
# https://docs.djangoproject.com/en/1.8/topics/auth/default/#django.contrib.auth.decorators.user_passes_test
#
# The decorator can either be applied to a view in urls.py
# or it can be added to the view classes 'dispatch' method.
# See the django docs, as it's a little weird.
#
# https://docs.djangoproject.com/en/1.8/topics/class-based-views/intro/#decorating-in-urlconf
# https://docs.djangoproject.com/en/1.8/topics/class-based-views/intro/#decorating-the-class
#
# So on the one hand, I think that permissions should be defined in
# the view, but on the other hand, at the moment the way you do that
# (by defining dispatch() specifically so that you can decorate it) is
# *really* ugly, one of the ugliest things in Django.
require_ava_superuser = django.contrib.auth.decorators.user_passes_test(is_ava_superuser)

# To create additional permissions checks, it might be easiest to copy
# this model: Create a simple true/false function like
# 'is_ava_superuser' above, and then create a decorator for it like
# 'require_ava_superuser'.


# Basic SMTP sending function to take inputs and format appropriately
def send_mail_smtp(address_to, address_from, message_subject, message_body):
    msg = MIMEMultipart('alternative')

    # Create message header
    msg['Subject'] = message_subject
    msg['From'] = address_from
    msg['To'] = address_to

    # Create message body
    msg.attach(MIMEText(message_body, 'plain'))

    # Get login details
    username = settings.MANDRILL_USERNAME
    password = settings.MANDRILL_PASSWORD

    # Log into mandrill
    s = smtplib.SMTP('smtp.mandrillapp.com', 587)
    s.login(username, password)

    # Send message
    #s.sendmail(msg['From'], msg['To'], msg.as_string())

    s.quit()