import json
from logging import getLogger

from django.conf import settings
from django.shortcuts import render, redirect
from django.views import generic

from .utils import handle_error, csrf_request, get_user_context, refresh_jwt_token

log = getLogger(__name__)


class AbstractObjectInterface(generic.TemplateView):
    url = settings.API_BASE_URL
    context = {}

    def get(self, request, *args, **kwargs):
        refresh_jwt_token(request)
        self.context['user'] = get_user_context(request)

    def post(self, request, **kwargs):
        refresh_jwt_token(request)
        self.context['user'] = get_user_context(request)


class ObjectIndex(AbstractObjectInterface):

    def get(self, request, template_name, url_suffix):
        super(ObjectIndex, self).get(request)
        log.debug(str(self.__class__) + " GET called")

        self.url = self.url + url_suffix

        log.debug(str(self.__class__) + " GET attempting to get data from url " + self.url)

        results = csrf_request(request=request, url=self.url, request_type='GET', is_authenticated=True)

        if results.status_code is 200:

            objects = results.json()
            log.debug(str(self.__class__) + " returned objects = " + str(objects))

            self.context['object_list'] = objects['results']

            return render(request, self.template_name, context=self.context)
        else:
            return handle_error(request, results.status_code)


class ObjectDetail(AbstractObjectInterface):

    def get(self, request, template_name, url_suffix, **kwargs):
        super(ObjectDetail, self).get(request)
        log.debug(str(self.__class__) + " GET called")

        self.url = self.url + url_suffix + '{}/'

        log.debug(str(self.__class__) + " Pre formatted url " + self.url)
        log.debug(str(self.__class__) + " kwargs " + str(self.kwargs))

        pk = self.kwargs.get('pk')
        self.url = self.url.format(pk)

        log.debug(str(self.__class__) + " GET attempting to get data from url " + self.url)

        results = csrf_request(request=request, url=self.url, request_type='GET', is_authenticated=True)

        if results.status_code is 200:
            log.debug(str(self.__class__) + " GET results = " + str(results))
            objects = results.json()

            log.debug(str(self.__class__) + " returned objects = " + str(objects))

            self.context['object'] = objects

            return render(request, self.template_name, context=self.context)
        else:
            return handle_error(request, results.status_code)


class ObjectCreate(AbstractObjectInterface):

    def get(self, request, template_name, url_suffix):
        super(ObjectCreate, self).get(request)
        render(request, self.template_name, context=self.context)

    def post(self, request, template_name, url_suffix, expected_fields, redirect_url, **kwargs):
        super(ObjectCreate, self).post(request, **kwargs)
        log.debug(str(self.__class__) + " POST called")

        self.url = self.url + url_suffix

        api_data = {}

        for field in expected_fields:
            # TODO explore validation here
            api_data[field] = request.POST.get(field)

        api_data = json.dumps(api_data)

        log.debug(str(self.__class__) + " POST attempting to get data from url " + self.url)
        log.debug(str(self.__class__) + " POST using the following api_data " + str(api_data))

        results = csrf_request(request=request, url=self.url, request_type='POST', api_data=api_data,
                               is_authenticated=True)

        log.debug(str(self.__class__) + " POST returned with status_code " + str(results.status_code))

        if results.status_code is 201:
            log.debug(str(self.__class__) + " POST results = " + str(results))

            objects = results.json()

            log.debug(str(self.__class__) + " returned objects = " + str(objects))

            self.context['object'] = objects

            return redirect(redirect_url)
        else:
            return handle_error(request, results.status_code)
