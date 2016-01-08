import json
import logging

import requests
from django.conf import settings
from django.shortcuts import render, redirect

log = logging.getLogger(__name__)





def csrf_request(request, url, request_type='POST', api_data={}, headers={}, is_authenticated=False):
    # add authorization header to existing headers if is_authenticated == True
    if is_authenticated is True:
        if 'token' in request.session:
            headers['Authorization'] = 'JWT ' + request.session['token']

        else:
            # TODO FIX THIS
            return handle_error(request=request, error_message='Not logged in', status_code='500', context=None)

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
        log.debug("Exception:: Connection Error " + e)
        return handle_error(None, '404')


def refresh_jwt_token(request):
    url = settings.API_BASE_URL + '/api-token-refresh/'

    headers = {'Content-Type': 'application/json'}

    if 'token' in request.session:
        data = {'token': request.session['token']}
        data = json.dumps(data)

        # log.debug("refresh_jwt_token :: Adding current token to request data :: " + str(data))
        try:
            results = requests.post(url, data=data, headers=headers)

            if results.status_code is 200:
                objects = results.json()
                request.session['token'] = objects['token']
                # log.debug("refresh_jwt_token :: Storing new token :: " + str(objects['token']))
            else:
                log.debug("refresh_jwt_token :: Failed to refresh token :: " + str(results.status_code) + "(" + str(
                    results.content) + ")")
        except ConnectionError as e:
            log.debug("Exception:: Connection Error " + e)
            return handle_error(None, '404')
    else:
        return redirect('login')
