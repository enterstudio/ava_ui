# Django Imports
from django.contrib import admin

from ava_ui.accounts.models import UserToken
# Local Imports

admin.site.register(UserToken)
