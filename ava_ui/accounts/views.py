import logging

from django.conf import settings
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render

from ava_ui.abstract.utils import handle_error, csrf_post_request, get_user_context

log = logging.getLogger(__name__)


def login(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')

        log.debug("Attempting to authenticate :: " + username)
        results = authenticate(request, username, password)
        log.debug("Authenticate returned :: " + str(results))

        if results is not None:

            if results.status_code == 200:
                content = results.json()
                request.session['token'] = content['token']
                request.session['user'] = username

                if request.POST.get("next") is not "":
                    log.debug("REDIRECTING TO NEXT " + str(request.POST.get("next")))
                    return redirect(request.POST.get("next"))
                else:
                    log.debug("REDIRECTING TO :: " + str(settings.LOGIN_REDIRECT_URL))
                    return redirect(settings.LOGIN_REDIRECT_URL, context=get_user_context(request))
            else:
                return handle_error(request, results.status_code)
        else:
            return HttpResponseRedirect('login')
    else:
        return render(request, 'accounts/login.html', context=get_user_context(request))


def authenticate(request, username, password):
    url = settings.API_BASE_URL + '/login/'
    login_data = {'username': username,
                  'password': password,
                  }
    return csrf_post_request(request=request, url=url, api_data=login_data)


def logout(request):
    request.session['token'] = None
    request.session['user'] = None
    return redirect('login')


def password_reset(request):
    template_name = 'accounts/password-reset.html'
    url = settings.API_BASE_URL + '/accounts/password/reset/'

    if request.POST:
        email = request.POST.get('email')
        api_data = {'email': email}
        results = csrf_post_request(request=request, url=url, api_data=api_data)

        if results is not None:
            if results.status_code == 200:
                return redirect(settings.LOGIN_REDIRECT_URL, context=get_user_context(request))
            else:
                return handle_error(request, results.status_code)
        else:
            return HttpResponseRedirect('login')
    else:
        return render(request, template_name, context=get_user_context(request))


def password_reset_token(request):
    reset_template_name = 'accounts/password-reset.html'
    url = settings.API_BASE_URL + '/accounts/password/reset/confirm/'

    if request.GET:
        token = request.GET.get('token')
        uid = request.GET.get('uid')
        api_data = {'token': token,
                    'uid': uid, }
        results = csrf_post_request(request=request, url=url, api_data=api_data)

        if results is not None:
            if results.status_code == 200:
                return redirect('password-reset-confirm')
            else:
                return handle_error(request, results.status_code)
        else:
            # TODO is this the right template to send this to?
            return render(request, reset_template_name, context=get_user_context(request))
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
        results = csrf_post_request(request=request, url=url, api_data=api_data)

        if results is not None:
            if results.status_code == 200:
                return redirect('password-reset-done')
            else:
                return handle_error(request, results.status_code)
        else:
            # TODO is this the right template to send this to?
            return render(request, reset_template_name, context=get_user_context(request))
    else:
        return render(request, template_name, context=get_user_context(request))


def password_reset_done(request):
    template_name = 'accounts/password-reset-done.html'
    return render(request, template_name, context=get_user_context(request))


def password_reset_complete(request):
    template_name = 'accounts/password-reset-complete.html'
    return render(request, template_name, context=get_user_context(request))


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
        results = csrf_post_request(request=request, url=url, api_data=api_data, is_authenticated=True)
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
        return render(request, template_name, context=get_user_context(request))


def password_change_done(request):
    template_name = 'accounts/password-change-done.html'
    return render(request, template_name, context=get_user_context(request))


def register(request):
    template_name = 'accounts/register.html'
    url = settings.API_BASE_URL + '/accounts/register/'

    if request.POST:
        log.debug("POST dictionary contains :: " + str(request.POST))

        email = request.POST.get('email')
        password = request.POST.get('password')

        api_data = {'username': email,
                    'email': email,
                    'password' : password}

        results = csrf_post_request(request=request, url=url, api_data=api_data, is_authenticated=False)
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
        return render(request, template_name, context=get_user_context(request))

def verify_email(request):
    template_name = 'accounts/verify.html'
    url = settings.API_BASE_URL + '/accounts/verify-email/'

    if request.GET:
        key = request.GET.get('key')

        api_data = {'key': key,}
        results = csrf_post_request(request=request, url=url, api_data=api_data)

        if results is not None:
            if results.status_code == 200:
                return render(request, template_name, context=get_user_context(request))
            else:
                return handle_error(request, results.status_code)
        else:
            # TODO is this the right template to send this to?
            return handle_error(request, results.status_code)
    else:
        return redirect('login')