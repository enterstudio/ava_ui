import json
import logging

import requests
from django.conf import settings
from django.shortcuts import redirect

from ava_ui.abstract.errors import handle_error, ErrorStatus

log = logging.getLogger(__name__)


def csrf_request(request, url, request_type='POST', api_data={}, headers={}, is_authenticated=False):
    # add authorization header to existing headers if is_authenticated == True
    if is_authenticated is True:
        if 'token' in request.session:
            headers['Authorization'] = 'JWT ' + request.session['token']

        else:
            return handle_error(request=request, error_message='No token found in session',
                                status_code=ErrorStatus.NOT_AUTHENTICATED)

    # add csrf header to existing headers
    if request:
        headers['HTTP_X_CSRFTOKEN'] = request.COOKIES['csrftoken']

    try:
        if request_type is 'POST':
            return requests.post(url, data=api_data, headers=headers)
        elif request_type is 'GET':
            return requests.get(url, headers=headers)
        elif request_type is 'DELETE':
            return requests.delete(url, headers=headers)
        elif request_type is 'PUT':
            return requests.put(url, data=api_data, headers=headers)
    except ConnectionError as e:
        return handle_error(request=request, error_message='Connection Error' + str(e),
                            status_code=ErrorStatus.SERVER_ERROR)


def refresh_jwt_token(request):
    url = settings.API_BASE_URL + '/api-token-refresh/'

    headers = {'Content-Type': 'application/json'}

    if 'token' in request.session:
        data = {'token': request.session['token']}
        data = json.dumps(data)

        try:
            results = requests.post(url, data=data, headers=headers)

            if results.status_code is 200:
                objects = results.json()
                request.session['token'] = objects['token']
            else:
                log.debug("refresh_jwt_token :: Failed to refresh token :: " + str(results.status_code) + "(" + str(
                    results.content) + ")")
        except ConnectionError as e:
            return handle_error(request=request, error_message='Connection Error' + str(e),
                                status_code=ErrorStatus.SERVER_ERROR)
    else:
        return redirect('login')
