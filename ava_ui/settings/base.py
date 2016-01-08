import enum
import os

## BASE_DIR is the path to the top level of the AVA project.
## That is: the root of the git repo, NOT the path to the
## AVA python package.
##
## The current layout is such that BASE_DIR is two directory
## levels up from the location of this settings file.
BASE_DIR = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__),
        '../..'
    )
)


SITE_ID=1

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'ava_ui.db'),
    },
}

API_BASE_URL = 'http://192.168.59.103:8000'
PUBLIC_BASE_URL = 'http://avasecure.com:8888'
LOGIN_REDIRECT_URL = PUBLIC_BASE_URL + '/organize/people/'

DEBUG = os.environ.get('DJANGO_DEBUG', 'true').lower() == 'true'
# TEMPLATE_DEBUG = DEBUG

# The model that is used to represent users
# The format of this value is '<package_label>.<model_name>'
USER_MODEL = 'auth.User'

# The ALLOWED_HOSTS setting is a security setting. It should be set
# with the host names that the application is expecting to receive
# requests as. For example 'localhost' and 'avasecure.com'.
#
# It's not checked unless DEBUG is turned off, and so we're using
# the liberal default of '*', this isn't appropriate for a production
# deployment.
#
# You can set custom hostnames using the DJANGO_ALLOWED_HOSTS environment
# variable in secrets.env
#
# See the link to the Django documentation for more details.
#
# https://docs.djangoproject.com/en/1.8/ref/settings/#allowed-hosts
DEFAULT_ALLOWED_HOSTS = '*'
ALLOWED_HOSTS = os.environ.get('DJANGO_ALLOWED_HOSTS',
                               DEFAULT_ALLOWED_HOSTS).strip().split()

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates'),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.request',
                'django.contrib.messages.context_processors.messages',
                'django.core.context_processors.request',
            ],
        },
    },
]


# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/
LANGUAGE_CODE = 'en-nz'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

SECRET_KEY = os.environ.get('DJANGO_APP_SECRET_KEY', '')

MIDDLEWARE_CLASSES = (

    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'csp.middleware.CSPMiddleware',
)

AUTHENTICATION_BACKENDS = (
    'ava_ui.accounts.authentication.APIAuthenticationBackend',
)

ROOT_URLCONF = 'ava_ui.urls'

DEFAULT_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
)

LOCAL_APPS = (
    'ava_ui.abstract',
    'ava_ui.organize',
    'ava_ui.gather.gather_google',
    'ava_ui.gather.gather_ldap',
    'ava_ui.learn',
    'ava_ui.my',
    'ava_ui.game',
    # 'ava_ui.notify',
    'ava_ui.integration.integration_google',
    'ava_ui.integration.integration_ldap',
    'ava_ui.evaluate',
    'ava_ui.accounts',
)

THIRD_PARTY_APPS = (
    # The Django sites framework is required
    'django.contrib.sites',
    'rest_framework',

    'corsheaders',

    'dh5bp',
    'bootstrap3',
    'bootstrapform',

)

INSTALLED_APPS = DEFAULT_APPS + THIRD_PARTY_APPS + LOCAL_APPS

REST_FRAMEWORK = {
    # Use Django's standard `django.contrib.auth` permissions,
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticatedOrReadOnly'
    ],
    'PAGE_SIZE': 10,
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.TokenAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
    )
}


## STATIC FILE CONFIGURATION
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler'
        },
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'devserver',
        },
    },
    'loggers': {
        'django.request': {
            'handlers': ['console', 'mail_admins'],
            'level': 'INFO',
            'propagate': True,
        },
        'ava_ui': {
            'handlers': ['console'],
            'level': 'DEBUG',
            'propogate': True,
        },
    },
    'formatters': {
        ## This formatter is intended to be reasonably verbose but readable when
        ## mixed in with the log messages the Django devserver spits out all the
        ## time.
        'devserver': {
            ## Format the date such that it matches the date format the Django
            ## Dev server spits out.
            'datefmt': '[%d/%b/%Y %H:%M:%S]',
            ## The whitespace gap after 'asctime' is just there to try
            ## and make the log a bit more visually distinctive from
            ## the 'access log' output on the dev server.
            'format': '%(asctime)s      %(levelname)s %(message)s (%(name)s:%(lineno)s)',
        },
    },
}

## REDIS CONFIGURATION
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



PUBLIC_SITE_URLS = [
    'http://localhost:8000/',
]


## CONTENT SECURITY POLICY (CSP) CONFIGURATION
##
## Here is where we configure exemptions from the default (strong)
## CSP policy. In an ideal world, this will be empty.
##
## Documented at: http://django-csp.readthedocs.org/en/latest/configuration.html
##
## CSP crash course at: http://django-csp.readthedocs.org/en/latest/configuration.html

CSP_STYLE_SRC = (
    ## 'self' is for all local assets, the usual default.
    "'self'",

    ## Unfortunately 'modernizr' seems to require 'unsafe-inline' styles.
    "'unsafe-inline'",

    ## CDN for a stylesheet we're pulling in.
    "http://maxcdn.bootstrapcdn.com/"
)

CSP_SCRIPT_SRC = (
    "'self'",
    ## lodash.min.js requires the use of 'unsafe-eval', which is a shame.
    "'unsafe-eval'",

    ## JQuery is being pulled from a CDN.
    "http://ajax.googleapis.com",

    ## This sha256 excemption is for the tiny little bit of javascript
    ## that the django-html5-boilerplate library is injecting at the
    ## bottom of seemingly every page. It would be nice for this to go
    ## away somehow.
    "'sha256-QElWz9ZyO3cMaja_DMF2vK4SfsTklXYMigNFQGuxka8='",
)

CSP_FONT_SRC = (
    "'self'",
    ## Bootstrap CDN
    "http://maxcdn.bootstrapcdn.com/",
)

CSP_IMG_SRC = (
    "'self'",

    ## This might not be necessary. Not having it in place was
    ## Causing a CSP violation because of an image Lastpass
    ## injects into form fields. If that's actually the only
    ## reason we're seeing those violations, than later we can
    ## remove this exemption again.
    "data:",
)

# DJANGO DEBUG TOOLBAR CONFIGURATION
def _show_toolbar_callback(request):
    toolbar_is_enabled = os.environ.get('ENABLE_DJANGO_DEBUG_TOOLBAR', 'false').lower() == 'true'
    return DEBUG and toolbar_is_enabled


DEBUG_TOOLBAR_CONFIG = {
    'SHOW_TOOLBAR_CALLBACK': _show_toolbar_callback,
}


try:
    from ava_ui.settings.local import *
except ImportError:
    pass
