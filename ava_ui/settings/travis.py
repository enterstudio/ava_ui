"""
This settings file is used during Travis CI runs.
"""

from .base import *  # noqa

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'ava_ui',
        'USER': 'postgres',
    }
}
