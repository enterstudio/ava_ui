# Django Imports
from django.apps import AppConfig


# Implementation
class MyConfig(AppConfig):
    name = 'ava.my'
    label = 'ava_user_profile'
    verbose_name = 'My Profile'

    def ready(self):
        pass
