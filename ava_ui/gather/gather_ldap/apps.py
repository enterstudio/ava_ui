# Django Imports
from django.apps import AppConfig


# Implementation
class MyConfig(AppConfig):
    name = 'ava.gather.ldap'
    label = 'ava_gather_ldap'
    verbose_name = 'Gather : LDAP'

    def ready(self):
        import ava.gather_ldap.signals
