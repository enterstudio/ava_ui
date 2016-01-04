import json
import logging

import requests
from django.conf import settings
from django.shortcuts import render

log = logging.getLogger(__name__)


def handle_error(request, status_code):
    log.debug("Called handle_error with status code :: " + str(status_code))
    if status_code is 401 or 403:
        #     return redirect('login')
        # else:
        return render(request, 'error/generic_error.html')


def csrf_request(request, url, request_type='POST', api_data={}, headers={}, is_authenticated=False, **kwargs):
    # add authorization header to existing headers if is_authenticated == True
    if is_authenticated is True:
        if 'token' in request.session:
            headers['Authorization'] = 'JWT ' + request.session['token']
        else:
            # TODO FIX THIS
            return handle_error(request, 'Not logged in')

    # add csrf header to existing headers
    headers['HTTP_X_CSRFTOKEN'] = request.COOKIES['csrftoken']
    # log.debug("csrf_post_request :: Adding CSRF token to headers :: " + str(headers['HTTP_X_CSRFTOKEN']))

    log.debug("csrf_request :: making " + request_type + " request to " + str(url) + " with " + str(api_data))

    if request_type is 'POST':
        return requests.post(url, data=api_data, headers=headers)
    elif request_type is 'GET':
        return requests.get(url, headers=headers)
    elif request_type is 'DELETE':
        return requests.delete(url, headers=headers)
    elif request_type is 'PUT':
        return requests.put(url, data=api_data, headers=headers)


def refresh_jwt_token(request):
    url = settings.API_BASE_URL + '/api-token-refresh/'

    headers = {'Content-Type': 'application/json'}

    data = {'token': request.session['token']}
    data = json.dumps(data)

    # log.debug("refresh_jwt_token :: Adding current token to request data :: " + str(data))

    results = requests.post(url, data=data, headers=headers)

    if results.status_code is 200:
        objects = results.json()
        request.session['token'] = objects['token']
        # log.debug("refresh_jwt_token :: Storing new token :: " + str(objects['token']))
    else:
        log.debug("refresh_jwt_token :: Failed to refresh token :: " + str(results.status_code) + "(" + str(
            results.content) + ")")


def get_user_context(request):
    context = {}
    if 'user' in request.session:
        context['user'] = request.session['user']
    else:
        context['user'] = None
    return context
