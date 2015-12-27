from logging import getLogger

import requests
from django.conf import settings
from django.shortcuts import render
from django.views import generic

from .utils import handle_error

log = getLogger(__name__)


class ObjectIndex(generic.TemplateView):
    url = settings.API_BASE_URL
    context = {}

    def get(self, request, template_name, url_suffix):
        log.debug(str(self.__class__) + " GET called")

        self.url = self.url + url_suffix
        self.context['user'] = request.session['user']

        log.debug(str(self.__class__) + " GET attempting to get data from url " + self.url)

        header = {'Authorization': 'JWT ' + request.session['token']}
        log.debug(str(self.__class__) + " JWT header = " + str(header))

        results = requests.get(self.url, headers=header)

        if results.status_code is 200:

            objects = results.json()

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
        self.context['user'] = request.session['user']

        log.debug(str(self.__class__) + " GET attempting to get data from url " + self.url)

        header = {'Authorization': 'JWT ' + request.session['token']}
        log.debug(str(self.__class__) + " JWT header = " + str(header))

        results = requests.get(self.url, headers=header)

        if results.status_code is 200:
            log.debug(str(self.__class__) + " GET results = " + str(results))
            objects = results.json()
            self.context['object'] = objects

            return render(request, self.template_name, context=self.context)
        else:
            return handle_error(request, results.status_code)
