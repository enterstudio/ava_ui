import logging

from django.conf import settings
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render

from ava_ui.abstract.utils import handle_error, csrf_request

log = logging.getLogger(__name__)


def login_ui(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')

        log.debug("Attempting to authenticate :: " + username)
        user = authenticate(username=username, password=password, request=request)
        if user:
            if user.is_active:
                try:
                    login(request, user)
                    log.debug("Request :: " + str(request.user))
                    log.debug("Is authenticated :: " + str(user.is_authenticated()))
                except Exception as e:
                    log.debug("Exception during login ::" + e)
        return redirect('learn-index')
    else:
        return render(request, 'accounts/login.html')


def logout_ui(request):
    request.session['token'] = None
    try:
        logout(request)
    except Exception as e:
        pass
    return redirect('login')


def password_reset(request):
    template_name = 'accounts/password-reset.html'
    url = settings.API_BASE_URL + '/accounts/password/reset/'

    if request.POST:
        email = request.POST.get('email')
        api_data = {'email': email}
        results = csrf_request(request=request, request_type='POST', url=url, api_data=api_data)

        if results is not None:
            if results.status_code == 200:
                return redirect(settings.LOGIN_REDIRECT_URL)
            else:
                return handle_error(request, results.status_code)
        else:
            return HttpResponseRedirect('login')
    else:
        return render(request, template_name)


def password_reset_token(request):
    reset_template_name = 'accounts/password-reset.html'
    url = settings.API_BASE_URL + '/accounts/password/reset/confirm/'

    if request.GET:
        token = request.GET.get('token')
        uid = request.GET.get('uid')
        api_data = {'token': token,
                    'uid': uid, }
        results = csrf_request(request=request, request_type='POST', url=url, api_data=api_data)

        if results is not None:
            if results.status_code == 200:
                return redirect('password-reset-confirm')
            else:
                return handle_error(request, results.status_code)
        else:
            # TODO is this the right template to send this to?
            return render(request, reset_template_name)
    else:
        return redirect('password-reset')


def password_reset_confirm(request):
    template_name = 'accounts/password-reset-confirm.html'
    reset_template_name = 'accounts/password-reset.html'
    url = settings.API_BASE_URL + '/accounts/password/reset/confirm/'

    if request.POST:
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        api_data = {'new_password1': password1,
                    'new_password2': password2, }
        results = csrf_request(request=request, request_type='POST', url=url, api_data=api_data)

        if results is not None:
            if results.status_code == 200:
                return redirect('password-reset-done')
            else:
                return handle_error(request, results.status_code)
        else:
            # TODO is this the right template to send this to?
            return render(request, reset_template_name)
    else:
        return render(request, template_name)


def password_reset_done(request):
    template_name = 'accounts/password-reset-done.html'
    return render(request, template_name)


def password_reset_complete(request):
    template_name = 'accounts/password-reset-complete.html'
    return render(request, template_name)


# TODO sort out authentication for this
# TODO I hate this workflow. This doesn't ask for the old password and is pretty nasty. Could do with replacing this
# TODO with an email verification thing like used for password reset
def password_change(request):
    template_name = 'accounts/password-change.html'
    url = settings.API_BASE_URL + '/accounts/password/change/'

    if request.POST:
        log.debug("POST dictionary contains :: " + str(request.POST))
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        api_data = {'new_password1': password1,
                    'new_password2': password2, }
        results = csrf_request(request=request, request_type='POST', url=url, api_data=api_data, is_authenticated=True)
        log.debug("password change returned :: " + str(results))
        if results is not None:
            if results.status_code == 200:
                return redirect('password-change-done')
            else:
                return handle_error(request, results.status_code)
        else:
            # TODO is this the right template to send this to?
            return handle_error(request, results.status_code)
    else:
        return render(request, template_name)


def password_change_done(request):
    template_name = 'accounts/password-change-done.html'
    return render(request, template_name)


def register(request):
    template_name = 'accounts/register.html'
    url = settings.API_BASE_URL + '/accounts/register/'

    if request.POST:
        log.debug("POST dictionary contains :: " + str(request.POST))

        email = request.POST.get('email')
        password = request.POST.get('password')

        api_data = {'username': email,
                    'email': email,
                    'password': password}

        results = csrf_request(request=request, request_type='POST', url=url, api_data=api_data, is_authenticated=False)
        log.debug("register returned :: " + str(results))
        if results is not None:
            if results.status_code == 200:
                return redirect('login')
            else:
                return handle_error(request, results.status_code)
        else:
            # TODO is this the right template to send this to?
            return handle_error(request, results.status_code)
    else:
        return render(request, template_name)


def verify_email(request):
    template_name = 'accounts/verify.html'
    url = settings.API_BASE_URL + '/accounts/verify-email/'

    if request.GET:
        key = request.GET.get('key')

        api_data = {'key': key, }
        results = csrf_request(request=request, request_type='POST', url=url, api_data=api_data)

        if results is not None:
            if results.status_code == 200:
                return render(request, template_name)
            else:
                return handle_error(request, results.status_code)
        else:
            # TODO is this the right template to send this to?
            return handle_error(request, results.status_code)
    else:
        return redirect('login')
