import logging

from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

from ava_ui.abstract.views import ObjectDetail, ObjectIndex

log = logging.getLogger(__name__)


class GoogleGatherImport(LoginRequiredMixin, PermissionRequiredMixin, ObjectDetail):
    permission_required = 'is_staff'
    url_suffix = '/gather/google/import/'
    template_name = "gather/google/google_dashboard.html"

    def get(self, request, **kwargs):
        return super(GoogleGatherImport, self).get(request, self.template_name, self.url_suffix, **kwargs)


class GoogleGatherIndex(LoginRequiredMixin, PermissionRequiredMixin, ObjectIndex):
    permission_required = 'is_staff'
    url_suffix = '/integration/google/setup/'
    template_name = "gather/google/google_dashboard.html"

    def get(self, request, **kwargs):
        return super(GoogleGatherIndex, self).get(request, self.template_name, self.url_suffix, **kwargs)
