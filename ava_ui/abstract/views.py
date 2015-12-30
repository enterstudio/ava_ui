from logging import getLogger

from django.conf import settings
from django.shortcuts import render, redirect
from django.views import generic

from .utils import handle_error, csrf_request, get_user_context

log = getLogger(__name__)


class ObjectIndex(generic.TemplateView):
    url = settings.API_BASE_URL
    context = {}

    def get(self, request, template_name, url_suffix):
        log.debug(str(self.__class__) + " GET called")

        self.url = self.url + url_suffix

        self.context['user'] = get_user_context(request)

        log.debug(str(self.__class__) + " GET attempting to get data from url " + self.url)

        results = csrf_request(request=request, url=self.url, request_type='GET', is_authenticated=True)

        if results.status_code is 200:

            objects = results.json()
            log.debug(str(self.__class__) + " returned objects = " + str(objects))

            self.context['object_list'] = objects['results']

            return render(request, self.template_name, context=self.context)
        else:
            return handle_error(request, results.status_code)


class ObjectDetail(generic.TemplateView):
    url = settings.API_BASE_URL
    context = {}

    def get(self, request, template_name, url_suffix, **kwargs):
        log.debug(str(self.__class__) + " GET called")

        self.url = self.url + url_suffix + '{}/'

        log.debug(str(self.__class__) + " Pre formatted url " + self.url)
        log.debug(str(self.__class__) + " kwargs " + str(self.kwargs))

        pk = self.kwargs.get('pk')
        self.url = self.url.format(pk)

        self.context = get_user_context(request)

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


class ObjectCreate(generic.TemplateView):
    url = settings.API_BASE_URL
    context = {}

    def get(self, request, template_name, url_suffix):
        self.context = get_user_context(request)
        render(request, self.template_name, context=self.context)

    def post(self, request, template_name, url_suffix, expected_fields, redirect_url, **kwargs):
        log.debug(str(self.__class__) + " POST called")

        self.url = self.url + url_suffix

        self.context = get_user_context(request)

        api_data = {}

        for field in expected_fields:
            # TODO explore validation here
            api_data[field] = request.POST.get(field)

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
