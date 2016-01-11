import logging

from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

from ava_ui.abstract.views import ObjectDetail, ObjectIndex

log = logging.getLogger(__name__)

class LDAPGatherImport(LoginRequiredMixin, PermissionRequiredMixin, ObjectDetail):
    permission_required = 'is_staff'
    url_suffix = '/gather/ldap/import/'
    template_name = "gather/ldap/ldap_dashboard.html"

    def get(self, request, **kwargs):
        return super(LDAPGatherImport, self).get(request, self.template_name, self.url_suffix, **kwargs)

class LDAPGatherIndex(LoginRequiredMixin, PermissionRequiredMixin, ObjectIndex):
    permission_required = 'is_staff'
    url_suffix = '/integration/ldap/setup/'
    template_name = "gather/ldap/ldap_dashboard.html"

    def get(self, request, **kwargs):
        return super(LDAPGatherIndex, self).get(request, self.template_name, self.url_suffix, **kwargs)