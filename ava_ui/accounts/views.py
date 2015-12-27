import logging

import requests
from django.conf import settings
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render

from ava_ui.abstract.utils import handle_error
from ava_ui.accounts.models import UserToken

log = logging.getLogger(__name__)


def login(request):
    context = {'user': None}
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']
        # log.debug("Request user before :: " + str(request.user))
        # log.debug("Request user is authenticated?? :: " + str(request.user.is_authenticated()))
        log.debug("Attempting to authenticate :: " + username)
        results = authenticate(request, username, password)
        log.debug("Authenticate returned :: " + str(results))

        if results is not None:
            # log.debug("Authenticate returned status code :: " + str(results.status_code))
            # log.debug("Authenticate returned content :: " + str(results.content))

            if results.status_code == 200:
                content = results.json()
                # log.debug("Request user after :: " + str(request.user))
                # log.debug("Request user is authenticated?? :: " + str(request.user.is_authenticated()))
                request.session['token'] = content['token']
                request.session['user'] = username
                context = {'user': username}
                if request.POST["next"] is not "":
                    log.debug("REDIRECTING TO NEXT " + str(request.POST["next"]))
                    return redirect(request.POST["next"])
                else:
                    log.debug("REDIRECTING TO :: " + str(settings.LOGIN_REDIRECT_URL))
                    return redirect(settings.LOGIN_REDIRECT_URL, context=context)
            else:
                return handle_error(request, results.status_code)
        else:
            return HttpResponseRedirect('login')
    else:
        return render(request, 'accounts/login.html', context=context)



def authenticate(request, username, password):
    url = settings.API_BASE_URL + '/login/'
    login_data = {'username': username,
                  'password': password,
                  }
    # csrf_headers = {'HTTP_X_CSRFTOKEN': request.COOKIES['csrftoken']}
    # log.debug("Attempting login with :: " + str(csrf_headers))
    # return requests.post(url, data=login_data, headers=csrf_headers)
    return requests.post(url, data=login_data)


def store_token(username, token):
    return UserToken.objects.update_or_create(owner=username, token=token)


def logout(request):
    request.session['token'] = None
    request.session['user'] = None
    return render(request, 'accounts/login.html')

# class password_change():
#
#     template_name = 'accounts/password-change.html'
#     name = 'password_change'
#
#
# class password_change_done():
#
#     template_name = 'accounts/password-change-done.html'
#     name = 'password_change_done'
#
#
# class password_reset():
#
#     template_name = 'accounts/password-reset.html'
#     name = 'password_reset'
#
#
# class password_reset_done():
#
#     template_name = 'accounts/password-reset-done.html', 'post_reset_redirect=' / '
#     name = 'password_reset_done'
