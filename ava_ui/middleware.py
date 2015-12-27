from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

import logging
log = logging.getLogger(__name__)


class AVARedirectionMiddleware(object):
    """Examine the request to see if the user needs to go somewhere else.

    Depending on various criteria, we may wish to redirect the user to
    somewhere else other than where they were trying to go. This
    middleware examines the request and either lets it fall through
    (by returning None) or it redirects the user to another URL.
    """

    def process_view(self, request, view_func, view_args, view_kwargs):

        # If no users exist: redirect to the create-superuser URL.
        create_first_user_uri = reverse('welcome-first-user')
        if (
                not request.user.is_authenticated() and
                not User.objects.exists() and
                not request.path == create_first_user_uri
        ):
            log.info("No AVA users: redirecting to 'create_first_user_uri'.")
            return HttpResponseRedirect(create_first_user_uri)

        return None
