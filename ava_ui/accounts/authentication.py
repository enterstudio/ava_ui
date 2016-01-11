import json
from logging import getLogger

from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.sessions.models import Session

from ava_ui.abstract.utils import csrf_request
from ava_ui.accounts.views import logout_ui

log = getLogger(__name__)


class APIAuthenticationBackend(object):
    def authenticate(self, username=None, password=None, request=None):
        url = settings.API_BASE_URL + '/login/'
        api_data = {'username': username,
                    'password': password,
                    }
        response = csrf_request(request=request, url=url, request_type='POST', api_data=api_data,
                                is_authenticated=False)
        # log.debug("Authenticate returned response " + str(response.status_code))
        if response.status_code is 200:
            content = response.json()
            # log.debug("Authenticate returned " + str(response.text))
            if request:
                request.session['token'] = content['token']
                # log.debug("Token returned from authenticate :: " + str(request.session['token']))
            return self.get_user_from_token(content['token'], request)
        return None

    def get_user(self, user_id):
        log.debug(" called get_user")
        if self.is_valid_token():
            try:
                user = User.objects.get(pk=user_id)
                log.debug(" called get_user and returned user: " + user.username)
                return user
            except User.DoesNotExist:
                log.debug(" called get_user and returned None")
                return None
        else:
            logout_ui(None)
            return None

    def is_valid_token(self):
        url = settings.API_BASE_URL + '/api-token-verify/'

        try:
            token = None
            session_objects = Session.objects.all()
            for objects in session_objects:
                if not token:
                    # log.debug("Examining session with pk :" + str(objects.pk))
                    # log.debug("Object :: " + str(objects.session_data))
                    session_data = objects.get_decoded()
                    # log.debug("Session data :: " + str(session_data))
                    token = session_data['token']

            api_data = {'token': token}

            response = csrf_request(request=None, url=url, api_data=api_data,
                                    request_type='POST',
                                    is_authenticated=False)
            log.debug("get_user_from_token returned response " + str(response))
            if response.status_code is 200:
                return True
            else:
                return False
        except Exception as e:
            log.debug("Exception in is_valid_token =  " + str(e))
            pass

        return False

    def get_user_from_token(self, token, request):
        url = settings.API_BASE_URL + '/accounts/user/token/'

        api_data = {'token': token}

        try:
            response = csrf_request(request=request, url=url, api_data=api_data,
                                    request_type='POST',
                                    is_authenticated=True)
            # log.debug("get_user_from_token returned response " + str(response))
            if response.status_code is 200:
                objects = response.json()

                user_data = objects['user']

                user_data = json.loads(user_data)

                # log.debug(" user_data :: " + str(user_data))

                try:
                    user = User.objects.get(username=user_data['username'])

                    # update the permissions on the user in case they have changed
                    user.is_staff = user_data['is_staff']
                    user.is_active = user_data['is_active']
                    user.is_superuser = user_data['is_superuser']
                    user.save()

                except User.DoesNotExist:
                    # Create a new user. Note that we can set password
                    # to anything, because it won't be checked; the password
                    # from settings.py will.
                    user = User(username=user_data['username'], password='NEVER CHECKED')
                    user.is_staff = user_data['is_staff']
                    user.is_active = user_data['is_active']
                    user.is_superuser = user_data['is_superuser']
                    user.save()

                return user

        except Exception as e:
            log.debug("Exception in get_user_from_token =  " + str(e))
            pass

        return None
