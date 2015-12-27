# Django Imports
from django.apps import AppConfig


# Implementation
class MyConfig(AppConfig):
    name = 'ava.game'
    label = 'ava_game'
    verbose_name = 'Game'

    def ready(self):
        import ava.game.signals
