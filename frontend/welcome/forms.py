import django.forms

from django.contrib.auth import forms as auth_forms
from django.contrib.auth import models as auth_models
from ava.core_auth import models as core_auth_models

import logging

log = logging.getLogger(__name__)


class CreateFirstSuperUser(auth_forms.UserCreationForm):
    # TODO: add any other interesting fields other than the defaults
    #       (username and password).

    def clean(self):
        # This form must never be 'valid' if any other users exist in
        # the system. It's a one-off for first-time AVA use.
        if auth_models.User.objects.exists():
            raise django.forms.ValidationError(
                'Initial user already exists.'
            )
        return super().clean()

    def save(self):
        assert self.is_valid(), "Attempted to call save() on invalid form"

        # Use the superclass's save() but don't commit to the db yet.
        user = super().save(commit=False)

        # Set the Django elevated privileges.
        user.is_staff = True
        user.is_superuser = True
        user.save()

        # Set the AVA elevated privilege, this implicitly creates the object.
        core_auth_models.UserRights.get(user)

        log.info("Created new AVA superuser: '%s'", user)
        return user
