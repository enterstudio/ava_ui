## REDIS CONFIGURATION
import enum
import os


class REDIS_DATABASES(enum.IntEnum):
    """Define slots for our redis databases."""
    DJANGO_CACHING_FRAMEWORK = 0
    DJANGO_SESSION_FRAMEWORK = 1
    CELERY_BROKER = 2
    CELERY_RESULT_BACKEND = 3


USE_REDIS_SESSIONS = False  # Turned off for the moment -- not needed.
if USE_REDIS_SESSIONS:
    SESSION_ENGINE = 'redis_sessions.session'
    SESSION_REDIS_HOST = os.environ.get('REDIS_PORT_6379_TCP_ADDR', 'localhost')
    SESSION_REDIS_PORT = os.environ.get('REDIS_PORT_6379_TCP_PORT', '6379')
    SESSION_REDIS_DB = int(REDIS_DATABASES.DJANGO_SESSION_FRAMEWORK)
    SESSION_REDIS_PREFIX = 'session'

## Using redis for the cache would be nice, but the library is still buggy
## with Python 3, When they fix the bugs hopefully we can just flip this
## switch.
USE_REDIS_CACHE = False  # Disabled because of Python 3 compatibility bugs.
if USE_REDIS_CACHE:
    CACHES = {
        'default': {
            'BACKEND': 'redis_cache.RedisCache',
            'LOCATION': (
                '{}:{}'.format(
                    os.environ.get('REDIS_PORT_6379_TCP_ADDR', 'localhost'),
                    os.environ.get('REDIS_PORT_6379_TCP_PORT', '6379'),
                )
            ),
            'OPTIONS': {
                'DB': REDIS_DATABASES.DJANGO_CACHING_FRAMEWORK,
            }
        },
    }

