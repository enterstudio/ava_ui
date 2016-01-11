import logging

from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin

from ava_ui.abstract.views import ObjectIndex, ObjectDetail, ObjectCreate, ObjectDelete, ObjectUpdate

log = logging.getLogger(__name__)


class LDAPIntegrationIndex(LoginRequiredMixin, PermissionRequiredMixin, ObjectIndex):
    permission_required = 'is_staff'
    url_suffix = '/integration/ldap/setup/'
    template_name = "integration/ldap/ldap_index.html"

    def get(self, request):
        return super(LDAPIntegrationIndex, self).get(request, self.template_name, self.url_suffix)


class LDAPIntegrationDetail(LoginRequiredMixin, PermissionRequiredMixin, ObjectDetail):
    permission_required = 'is_staff'
    url_suffix = '/integration/ldap/setup/'
    template_name = "integration/ldap/ldap_detail.html"

    def get(self, request, **kwargs):
        return super(LDAPIntegrationDetail, self).get(request, self.template_name, self.url_suffix, **kwargs)


class LDAPIntegrationCreate(LoginRequiredMixin, PermissionRequiredMixin, ObjectCreate):
    permission_required = 'is_staff'
    url_suffix = '/integration/ldap/setup/'
    template_name = "integration/ldap/ldap_form.html"

    def get(self, request):
        return super(LDAPIntegrationCreate, self).get(request, self.template_name, self.url_suffix)

    def post(self, request, **kwargs):
        expected_fields = ['name', 'dump_dn', 'server', 'ldap_password', 'ldap_user']
        redirect_url = 'integration-ldap-index'
        return super(LDAPIntegrationCreate, self).post(request=request, template_name=self.template_name,
                                                       url_suffix=self.url_suffix,
                                                       expected_fields=expected_fields,
                                                       redirect_url=redirect_url,
                                                       **kwargs)


class LDAPIntegrationUpdate(LoginRequiredMixin, PermissionRequiredMixin, ObjectUpdate):
    url_suffix = '/integration/ldap/setup/'
    template_name = "integration/ldap/ldap_form.html"

    def get(self, request, **kwargs):
        return super(LDAPIntegrationUpdate, self).get(request, self.template_name, self.url_suffix, **kwargs)

    def post(self, request, **kwargs):
        expected_fields = ['name', 'dump_dn', 'server', 'ldap_password', 'ldap_user']
        redirect_url = 'integration-ldap-index'
        return super(LDAPIntegrationUpdate, self).post(request=request, template_name=self.template_name,
                                                       url_suffix=self.url_suffix,
                                                       expected_fields=expected_fields,
                                                       redirect_url=redirect_url,
                                                       **kwargs)


class LDAPIntegrationDelete(LoginRequiredMixin, PermissionRequiredMixin, ObjectDelete):
    url_suffix = '/integration/ldap/setup/'
    redirect_url = 'integration-ldap-index'

    def get(self, request, **kwargs):
        return super(LDAPIntegrationDelete, self).get(request=request,
                                                      url_suffix=self.url_suffix,
                                                      redirect_url=self.redirect_url,
                                                      **kwargs)
