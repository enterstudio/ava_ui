# Django Imports
from django.apps import AppConfig


# Implementation
class MyConfig(AppConfig):
    name = 'ava.gather.google'
    label = 'ava_gather_google'
    verbose_name = 'Gather : Google'

    def ready(self):
        import ava.gather_google.signals
