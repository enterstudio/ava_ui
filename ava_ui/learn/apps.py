# Django Imports
from django.apps import AppConfig


# Implementation
class MyConfig(AppConfig):
    name = 'ava.learn'
    label = 'ava_learn'
    verbose_name = 'Learn'

    def ready(self):
        import ava.learn.signals
