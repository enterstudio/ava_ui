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


class ObjectUpdate(ObjectDetail):
    def get(self, request, template_name, url_suffix, **kwargs):
        return super(ObjectUpdate, self).get(request, template_name, url_suffix, **kwargs)

    def post(self, request, template_name, url_suffix, expected_fields, redirect_url, **kwargs):
        super(ObjectUpdate, self).post(request, **kwargs)
        log.debug(str(self.__class__) + " POST called")

        self.url = self.url + url_suffix + '{}/'

        log.debug(str(self.__class__) + " Pre formatted url " + self.url)

        pk = self.kwargs.get('pk')
        self.url = self.url.format(pk)

        api_data = {}

        for field in expected_fields:
            # TODO explore validation here
            api_data[field] = request.POST.get(field)

        api_data = json.dumps(api_data)

        log.debug(str(self.__class__) + " POST attempting to get data from url " + self.url)
        log.debug(str(self.__class__) + " POST using the following api_data " + str(api_data))

        headers = {'Content-Type': 'application/json'}

        results = csrf_request(request=request, url=self.url, request_type='PUT', api_data=api_data, headers=headers,
                               is_authenticated=True)

        log.debug(str(self.__class__) + " POST returned with status_code " + str(results.status_code))

        if results.status_code is 200:
            log.debug(str(self.__class__) + " POST results = " + str(results))
            #TODO might actually want to redirect to the details page here instead of the index
            return redirect(redirect_url)
        else:
            return handle_error(request, results.status_code)

class ObjectCreate(AbstractObjectInterface):
    def get(self, request, template_name, url_suffix):
        super(ObjectCreate, self).get(request)
        return render(request, self.template_name, context=self.context)

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

        headers = {'Content-Type': 'application/json'}

        results = csrf_request(request=request, url=self.url, request_type='POST', api_data=api_data, headers=headers,
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


class ObjectDelete(AbstractObjectInterface):
    def get(self, request, redirect_url, url_suffix, **kwargs):
        super(ObjectDelete, self).get(request)
        log.debug(str(self.__class__) + " POST called")

        self.url = self.url + url_suffix + '{}/'

        log.debug(str(self.__class__) + " Pre formatted url " + self.url)

        pk = self.kwargs.get('pk')
        self.url = self.url.format(pk)

        log.debug(str(self.__class__) + " POST attempting to delete object using url " + self.url)

        results = csrf_request(request=request, url=self.url, request_type='DELETE', is_authenticated=True)

        if results.status_code is 204:
            log.debug(str(self.__class__) + " POST results = " + str(results))
            return redirect(to=redirect_url)
        else:
            return handle_error(request, results.status_code)


class ObjectAuthorize(AbstractObjectInterface):
    def get(self, request, template_name, url_suffix, **kwargs):
        super(ObjectAuthorize, self).get(request)
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

            authorize_url = results.json()['authorize_url']

            log.debug(str(self.__class__) + " returned url = " + str(authorize_url))

            return redirect(authorize_url)
        else:
            return handle_error(request, results.status_code)


class ObjectAuthorizeCallback(AbstractObjectInterface):
    def get(self, request, template_name, url_suffix, **kwargs):
        super(ObjectAuthorizeCallback, self).get(request)
        log.debug(str(self.__class__) + " GET called")

        self.url = self.url + url_suffix + '{}/'

        log.debug(str(self.__class__) + " Pre formatted url " + self.url)
        log.debug(str(self.__class__) + " kwargs " + str(self.kwargs))

        code = request.GET.get('code')
        self.url = self.url.format(code)

        log.debug(str(self.__class__) + " GET attempting to get data from url " + self.url)

        results = csrf_request(request=request, url=self.url, request_type='GET', is_authenticated=True)

        if results.status_code is 200:
            log.debug(str(self.__class__) + " GET results = " + str(results))

            return render(request, self.template_name, context=self.context)
        else:
            return handle_error(request, results.status_code)
