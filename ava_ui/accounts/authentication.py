import json
from logging import getLogger

from django.conf import settings
from django.contrib.auth.models import User

from ava_ui.abstract.utils import csrf_request
from ava_ui.accounts.serializers import UserSerializer

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
        try:
            user = User.objects.get(pk=user_id)
            log.debug(" called get_user and returned user: "+ user.username)
        except User.DoesNotExist:
            log.debug(" called get_user and returned None")
            return None

    def get_user_from_token(self, token, request):
        url = settings.API_BASE_URL + '/accounts/user/token/'

        api_data = {'token': token}

        try:
            response = csrf_request(request=request, url=url, api_data=api_data,
                                    request_type='POST',
                                    is_authenticated=True)
            log.debug("get_user_from_token returned response " + str(response))
            if response.status_code is 200:
                objects = response.json()

                user_data = objects['user']

                user_data = json.loads(user_data)

                # users = User.objects.all()
                # log.debug("Users :: " + str(users))
                try:
                    user = User.objects.get(username=user_data['username'])
                    if user:
                        user.delete()
                except Exception as e:
                    pass

                # log.debug("get_user_from_token :: user_data =  " + str(user_data))

                user_serializer = UserSerializer(data=user_data)
                log.debug("Applying validation to user :: " + repr(user_serializer))
                if user_serializer.is_valid():
                    user = user_serializer.save()
                    log.debug("get_user_from_token username = " + str(user.username))
                    return user

        except Exception as e:
            log.debug("Exception in get_user_from_token =  " + str(e))
            pass

        return None
