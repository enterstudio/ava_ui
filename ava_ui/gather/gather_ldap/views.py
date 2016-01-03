import logging

from ava_ui.abstract.views import ObjectDetail, ObjectIndex

log = logging.getLogger(__name__)

class LDAPGatherImport(ObjectDetail):
    url_suffix = '/gather/ldap/import/'
    template_name = "gather/ldap/ldap_dashboard.html"

    def get(self, request, **kwargs):
        return super(LDAPGatherImport, self).get(request, self.template_name, self.url_suffix, **kwargs)

class LDAPGatherIndex(ObjectIndex):
    url_suffix = '/gather/ldap/'
    template_name = "gather/ldap/ldap_dashboard.html"

    def get(self, request, **kwargs):
        return super(LDAPGatherIndex, self).get(request, self.template_name, self.url_suffix, **kwargs)