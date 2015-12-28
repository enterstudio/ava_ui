import logging

import requests
from django.shortcuts import render, redirect

log = logging.getLogger(__name__)


def handle_error(request, status_code):
    log.debug("Called handle_error with status code :: " + str(status_code))
    if status_code is '401' or '403':
        return redirect('login')
    else:
        return render(request, 'error/generic_error.html')


def csrf_post_request(request, url, api_data, headers):
    # add csrf header to existing headers
    headers['HTTP_X_CSRFTOKEN'] = request.COOKIES['csrftoken']
    log.debug("csrf_post_request :: Adding CSRF token to headers :: " + str(headers['HTTP_X_CSRFTOKEN']))

    log.debug("csrf_post_request :: making POST request to " + str(url))
    return requests.post(url, data=api_data, headers=headers)


def get_user_context(request):
    context = {}
    if request.session['user']:
        context['user'] = request.session['user']
    else:
        context['user'] = None
    return context
