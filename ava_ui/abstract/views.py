import json
from logging import getLogger

from django.conf import settings
from django.shortcuts import render, redirect
from django.views import generic

from ava_ui.abstract.errors import handle_error
from .utils import csrf_request, refresh_jwt_token

log = getLogger(__name__)


class AbstractObjectInterface(generic.TemplateView):
    url = settings.API_BASE_URL
    context = {}

    def get(self, request, *args, **kwargs):
        refresh_jwt_token(request)
        self.context = self.get_context_data()

    def post(self, request, **kwargs):
        refresh_jwt_token(request)
        self.context = self.get_context_data()

    def get_context_data(self, **kwargs):
        return super(AbstractObjectInterface, self).get_context_data()


class ObjectIndex(AbstractObjectInterface):
    def get(self, request, template_name, url_suffix):
        super(ObjectIndex, self).get(request)

        self.url = self.url + url_suffix

        results = csrf_request(request=request, url=self.url, request_type='GET', is_authenticated=True)

        if results.status_code is 200:

            objects = results.json()
            self.context['object_list'] = objects['results']

            return render(request, self.template_name, context=self.context)
        else:
            return handle_error(request=request, error_message=results.text,
                                status_code=results.status_code)


class ObjectDashboard(AbstractObjectInterface):
    def get(self, request, template_name, url_suffix):
        super(ObjectDashboard, self).get(request)
        return render(request, self.template_name)


class ObjectDetail(AbstractObjectInterface):
    def get(self, request, template_name, url_suffix, **kwargs):
        super(ObjectDetail, self).get(request)

        self.url = self.url + url_suffix + '{}/'

        pk = self.kwargs.get('pk')
        self.url = self.url.format(pk)

        results = csrf_request(request=request, url=self.url, request_type='GET', is_authenticated=True)

        if results.status_code is 200:
            objects = results.json()

            self.context['object'] = objects

            return render(request, self.template_name, context=self.context)
        else:
            return handle_error(request=request, error_message=results.text,
                                status_code=results.status_code)


class ObjectUpdate(ObjectDetail):
    def get(self, request, template_name, url_suffix, form_data_url_suffix=None, **kwargs):
        super(ObjectUpdate, self).get(request, template_name, url_suffix, **kwargs)

        if form_data_url_suffix:
            self.url = self.url + form_data_url_suffix

            results = csrf_request(request=request, url=self.url, request_type='GET', is_authenticated=True)

            if results.status_code is 200:

                try:
                    objects = results.json()
                    self.context['form_data'] = objects['form_data']

                except Exception as e:
                    return handle_error(request=request, error_message=str(e),
                                        status_code=results.status_code)
            else:
                return handle_error(request=request, error_message=results.text,
                                    status_code=results.status_code)
        return render(request, self.template_name, context=self.context)

    def post(self, request, template_name, url_suffix, expected_fields, redirect_url, **kwargs):
        super(ObjectUpdate, self).post(request, **kwargs)

        self.url = self.url + url_suffix + '{}/'

        pk = self.kwargs.get('pk')
        self.url = self.url.format(pk)

        api_data = {}

        for field in expected_fields:
            # TODO explore validation here
            api_data[field] = request.POST.get(field)

        api_data = json.dumps(api_data)

        headers = {'Content-Type': 'application/json'}

        results = csrf_request(request=request, url=self.url, request_type='PUT', api_data=api_data, headers=headers,
                               is_authenticated=True)

        if results.status_code is 200:
            # TODO might actually want to redirect to the details page here instead of the index
            return redirect(redirect_url)
        else:
            return handle_error(request=request, error_message=results.text,
                                status_code=results.status_code)


class ObjectCreate(AbstractObjectInterface):
    def get(self, request, template_name, form_data_url_suffix=None):
        super(ObjectCreate, self).get(request)
        if form_data_url_suffix:
            self.url = self.url + form_data_url_suffix

            results = csrf_request(request=request, url=self.url, request_type='GET', is_authenticated=True)

            if results.status_code is 200:

                try:
                    objects = results.json()
                    self.context['form_data'] = objects['form_data']
                    self.context['object'] = None

                except Exception as e:
                    return handle_error(request=request, error_message=str(e),
                                        status_code=results.status_code)
            else:
                return handle_error(request=request, error_message=results.text,
                                    status_code=results.status_code)
        return render(request, self.template_name, context=self.context)

    def post(self, request, template_name, url_suffix, expected_fields, redirect_url, **kwargs):
        super(ObjectCreate, self).post(request, **kwargs)

        self.url = self.url + url_suffix

        api_data = {}

        for field in expected_fields:
            # TODO explore validation here
            api_data[field] = request.POST.get(field)

        api_data = json.dumps(api_data)

        headers = {'Content-Type': 'application/json'}

        results = csrf_request(request=request, url=self.url, request_type='POST', api_data=api_data, headers=headers,
                               is_authenticated=True)

        if results.status_code is 201:

            objects = results.json()
            self.context['object'] = objects

            return redirect(redirect_url)
        else:
            return handle_error(request=request, error_message=results.text,
                                status_code=results.status_code)


class ObjectCreateRelated(AbstractObjectInterface):
    def get(self, request, template_name, url_suffix):
        super(ObjectCreateRelated, self).get(request)

        self.url = self.url + url_suffix

        results = csrf_request(request=request, url=self.url, request_type='GET', is_authenticated=True)

        if results.status_code is 200:

            try:
                objects = results.json()
                self.context['form_data'] = objects['form_data']
                self.context['object'] = None

                return render(request, self.template_name, context=self.context)
            except Exception as e:
                return handle_error(request=request, error_message=str(e),
                                    status_code=results.status_code)
        else:
            return handle_error(request=request, error_message=results.text,
                                status_code=results.status_code)

    def post(self, request,
             template_name, url_suffix, expected_fields,
             related_fields, redirect_url,
             multiple_fields=[], **kwargs):
        super(ObjectCreateRelated, self).post(request, **kwargs)

        self.url = self.url + url_suffix

        api_data = {}

        for field in expected_fields:
            # TODO explore validation here
            if field in related_fields:
                if field in request.POST:
                    api_data[field] = int(request.POST.get(field))
                else:
                    api_data[field] = None

            else:
                if field in request.POST:
                    api_data[field] = request.POST.get(field)
                else:
                    api_data[field] = None

        # log.debug(" POST data " + str(request.POST))
        for field in multiple_fields:
            if field in request.POST:
                string_values = request.POST.getlist(field)
                int_values = []
                for value in string_values:
                    int_values.append(int(value))
                api_data[field] = int_values

        api_data = json.dumps(api_data)

        headers = {'Content-Type': 'application/json'}

        results = csrf_request(request=request, url=self.url, request_type='POST', api_data=api_data, headers=headers,
                               is_authenticated=True)

        if results.status_code is 201:

            objects = results.json()

            self.context['object'] = objects

            return redirect(redirect_url)
        else:
            return handle_error(request=request, error_message=results.text,
                                status_code=results.status_code)


class ObjectUpdateRelated(AbstractObjectInterface):
    def get(self, request, template_name, url_suffix, form_data_url_suffix, **kwargs):
        super(ObjectUpdateRelated, self).get(request)

        url = self.url + url_suffix + '{}/'

        pk = self.kwargs.get('pk')
        url = url.format(pk)

        results = csrf_request(request=request, url=url, request_type='GET', is_authenticated=True)

        if results.status_code is 200:
            objects = results.json()
            self.context['object'] = objects

        url = self.url + form_data_url_suffix

        results = csrf_request(request=request, url=url, request_type='GET', is_authenticated=True)

        if results.status_code is 200:

            try:
                objects = results.json()

                self.context['form_data'] = objects['form_data']

            except Exception as e:
                return handle_error(request=request, error_message=results.text,
                                    status_code=results.status_code)
        else:
            return handle_error(request=request, error_message=results.text,
                                status_code=results.status_code)

        return render(request, self.template_name, context=self.context)

    def post(self, request, template_name, url_suffix, expected_fields, related_fields, redirect_url,
             multiple_fields=[], **kwargs):
        super(ObjectUpdateRelated, self).post(request, **kwargs)

        url = self.url + url_suffix + '{}/'

        pk = self.kwargs.get('pk')
        url = url.format(pk)

        api_data = {}

        for field in expected_fields:
            # TODO explore validation here
            if field in related_fields:
                if field in request.POST:
                    api_data[field] = int(request.POST.get(field))
                else:
                    api_data[field] = None

            else:
                if field in request.POST:
                    api_data[field] = request.POST.get(field)
                else:
                    api_data[field] = None

        # log.debug(" POST data " + str(request.POST))
        for field in multiple_fields:
            if field in request.POST:
                string_values = request.POST.getlist(field)
                int_values = []
                for value in string_values:
                    int_values.append(int(value))
                api_data[field] = int_values

        api_data = json.dumps(api_data)

        headers = {'Content-Type': 'application/json'}

        results = csrf_request(request=request, url=url, request_type='PUT', api_data=api_data, headers=headers,
                               is_authenticated=True)

        if results.status_code is 200:
            return redirect(redirect_url)
        else:
            return handle_error(request=request, error_message=results.text,
                                status_code=results.status_code)


class ObjectDelete(AbstractObjectInterface):
    def get(self, request, redirect_url, url_suffix, **kwargs):
        super(ObjectDelete, self).get(request)

        self.url = self.url + url_suffix + '{}/'

        pk = self.kwargs.get('pk')
        self.url = self.url.format(pk)

        results = csrf_request(request=request, url=self.url, request_type='DELETE', is_authenticated=True)

        if results.status_code is 204:
            return redirect(to=redirect_url)
        else:
            return handle_error(request=request, error_message=results.text,
                                status_code=results.status_code)


class ObjectAuthorize(AbstractObjectInterface):
    def get(self, request, template_name, url_suffix, **kwargs):
        super(ObjectAuthorize, self).get(request)

        self.url = self.url + url_suffix + '{}/'

        pk = self.kwargs.get('pk')
        self.url = self.url.format(pk)

        results = csrf_request(request=request, url=self.url, request_type='GET', is_authenticated=True)

        if results.status_code is 200:

            authorize_url = results.json()['authorize_url']

            return redirect(authorize_url)
        else:
            return handle_error(request=request, error_message=results.text,
                                status_code=results.status_code)


class ObjectAuthorizeCallback(AbstractObjectInterface):
    def get(self, request, template_name, url_suffix, **kwargs):
        super(ObjectAuthorizeCallback, self).get(request)

        self.url = self.url + url_suffix + '{}/'

        code = request.GET.get('code')
        self.url = self.url.format(code)

        results = csrf_request(request=request, url=self.url, request_type='GET', is_authenticated=True)

        if results.status_code is 200:
            return render(request, self.template_name, context=self.context)
        else:
            return handle_error(request=request, error_message=results.text,
                                status_code=results.status_code)
