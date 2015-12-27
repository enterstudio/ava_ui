# Django Imports
from django.apps import AppConfig


# Implementation
class MyConfig(AppConfig):
    name = 'ava.notify'
    label = 'ava_notify'
    verbose_name = 'Notify'

    def ready(self):
        import ava.notify.signals
