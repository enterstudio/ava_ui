# Django Imports
from django.apps import AppConfig


# Implementation
class MyConfig(AppConfig):
    name = 'ava.integration.google'
    label = 'ava_oauth_google'
    verbose_name = 'integration_google'

    def ready(self):
        import ava.oauth_google.signals
