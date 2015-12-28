import logging

from django.conf import settings
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render

from ava_ui.abstract.utils import handle_error, csrf_post_request, get_user_context
from ava_ui.accounts.models import UserToken

log = logging.getLogger(__name__)


def login(request):
    context = get_user_context()
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']

        log.debug("Attempting to authenticate :: " + username)
        results = authenticate(username, password)
        log.debug("Authenticate returned :: " + str(results))

        if results is not None:

            if results.status_code == 200:
                content = results.json()
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


def authenticate(username, password):
    url = settings.API_BASE_URL + '/login/'
    login_data = {'username': username,
                  'password': password,
                  }
    return csrf_post_request(url, data=login_data, headers={})


def store_token(username, token):
    return UserToken.objects.update_or_create(owner=username, token=token)


def logout(request):
    request.session['token'] = None
    request.session['user'] = None
    return render(request, 'accounts/login.html')


def password_reset(request):
    template_name = 'accounts/password-reset.html'
    url = settings.API_BASE_URL + '/password/reset/'

    if request.POST:
        email = request.POST['email']
        api_data = {'email': email}
        results = csrf_post_request(url, data=api_data, headers={})

        if results is not None:
            if results.status_code == 200:
                return redirect(settings.LOGIN_REDIRECT_URL, context=get_user_context())
            else:
                return handle_error(request, results.status_code)
        else:
            return HttpResponseRedirect('login')
    else:
        return render(request, template_name, context=get_user_context())


def password_reset_token(request):
    reset_template_name = 'accounts/password-reset.html'
    url = settings.API_BASE_URL + '/accounts/password/reset/confirm/'

    if request.GET:
        token = request.POST['token']
        uid = request.POST['uid']
        api_data = {'token': token,
                    'uid': uid, }
        results = csrf_post_request(url, data=api_data, headers={})

        if results is not None:
            if results.status_code == 200:
                return redirect('password-reset-confirm')
            else:
                return handle_error(request, results.status_code)
        else:
            # TODO is this the right template to send this to?
            return render(request, reset_template_name, context=get_user_context())
    else:
        return redirect('password-reset')


def password_reset_confirm(request):
    template_name = 'accounts/password-reset-confirm.html'
    reset_template_name = 'accounts/password-reset.html'
    url = settings.API_BASE_URL + '/accounts/password/reset/confirm/'

    if request.POST:
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        api_data = {'new_password1': password1,
                    'new_password2': password2, }
        results = csrf_post_request(url, data=api_data, headers={})

        if results is not None:
            if results.status_code == 200:
                return redirect('password-reset-done')
            else:
                return handle_error(request, results.status_code)
        else:
            # TODO is this the right template to send this to?
            return render(request, reset_template_name, context=get_user_context())
    else:
        return render(request, template_name, context=get_user_context())


def password_reset_done(request):
    template_name = 'accounts/password-reset-done.html'
    return render(request, template_name, context=get_user_context())


def password_reset_complete(request):
    template_name = 'accounts/password-reset-complete.html'
    return render(request, template_name, context=get_user_context())


# TODO sort out authentication for this
def password_change(request):
    template_name = 'accounts/password-change.html'
    url = settings.API_BASE_URL + '/accounts/password/change/'

    if request.POST:
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        api_data = {'new_password1': password1,
                    'new_password2': password2, }
        results = csrf_post_request(url, data=api_data, headers={})

        if results is not None:
            if results.status_code == 200:
                return redirect('password-change-done')
            else:
                return handle_error(request, results.status_code)
        else:
            # TODO is this the right template to send this to?
            return handle_error(request, results.status_code)
    else:
        return render(request, template_name, context=get_user_context())


def password_change_done(request):
    template_name = 'accounts/password-change-done.html'
    return render(request, template_name, context=get_user_context())
