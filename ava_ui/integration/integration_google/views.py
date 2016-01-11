import logging

from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

from ava_ui.abstract.views import ObjectIndex, ObjectDetail, ObjectCreate, ObjectDelete, ObjectAuthorize, \
    ObjectAuthorizeCallback, ObjectUpdate

log = logging.getLogger(__name__)


class GoogleIntegrationIndex(LoginRequiredMixin, PermissionRequiredMixin, ObjectIndex):
    permission_required = 'is_staff'
    url_suffix = '/integration/google/setup/'
    template_name = "integration/google/google_index.html"

    def get(self, request):
        return super(GoogleIntegrationIndex, self).get(request, self.template_name, self.url_suffix)


class GoogleIntegrationDetail(LoginRequiredMixin, PermissionRequiredMixin, ObjectDetail):
    permission_required = 'is_staff'
    url_suffix = '/integration/google/setup/'
    template_name = "integration/google/google_detail.html"

    def get(self, request, **kwargs):
        return super(GoogleIntegrationDetail, self).get(request, self.template_name, self.url_suffix, **kwargs)


class GoogleIntegrationCreate(LoginRequiredMixin, PermissionRequiredMixin, ObjectCreate):
    permission_required = 'is_staff'
    url_suffix = '/integration/google/setup/'
    template_name = "integration/google/google_form.html"

    def get(self, request):
        return super(GoogleIntegrationCreate, self).get(request, self.template_name, self.url_suffix)

    def post(self, request, **kwargs):
        expected_fields = ['name', 'description', 'domain']
        redirect_url = 'integration-google-index'
        return super(GoogleIntegrationCreate, self).post(request=request, template_name=self.template_name,
                                                         url_suffix=self.url_suffix,
                                                         expected_fields=expected_fields,
                                                         redirect_url=redirect_url,
                                                         **kwargs)


class GoogleIntegrationUpdate(LoginRequiredMixin, PermissionRequiredMixin, ObjectUpdate):
    permission_required = 'is_staff'
    url_suffix = '/integration/google/setup/'
    template_name = "integration/google/google_form.html"

    def get(self, request, **kwargs):
        return super(GoogleIntegrationUpdate, self).get(request, self.template_name, self.url_suffix, **kwargs)

    def post(self, request, **kwargs):
        expected_fields = ['name', 'description', 'domain']
        redirect_url = 'integration-google-index'
        return super(GoogleIntegrationUpdate, self).post(request=request, template_name=self.template_name,
                                                         url_suffix=self.url_suffix,
                                                         expected_fields=expected_fields,
                                                         redirect_url=redirect_url,
                                                         **kwargs)


class GoogleIntegrationDelete(LoginRequiredMixin, PermissionRequiredMixin, ObjectDelete):
    permission_required = 'is_staff'
    url_suffix = '/integration/google/setup/'
    redirect_url = 'integration-google-index'

    def get(self, request, **kwargs):
        return super(GoogleIntegrationDelete, self).get(request=request,
                                                        url_suffix=self.url_suffix,
                                                        redirect_url=self.redirect_url,
                                                        **kwargs)


class GoogleIntegrationAuthorize(LoginRequiredMixin, PermissionRequiredMixin, ObjectAuthorize):
    permission_required = 'is_staff'
    url_suffix = '/integration/google/redirect/'
    template_name = "integration/google/google_index.html"

    def get(self, request, **kwargs):
        return super(GoogleIntegrationAuthorize, self).get(request, self.template_name, self.url_suffix, **kwargs)


class GoogleIntegrationAuthorizeCallback(LoginRequiredMixin, PermissionRequiredMixin, ObjectAuthorizeCallback):
    permission_required = 'is_staff'
    url_suffix = '/integration/google/callback/?code='
    template_name = "integration/google/google_index.html"

    def get(self, request, **kwargs):
        return super(GoogleIntegrationAuthorizeCallback, self).get(request, self.template_name, self.url_suffix,
                                                                   **kwargs)
