import logging

from ava_ui.abstract.views import ObjectDetail, ObjectIndex

log = logging.getLogger(__name__)


class GoogleGatherImport(ObjectDetail):
    url_suffix = '/gather/google/import/'
    template_name = "gather/google/google_dashboard.html"

    def get(self, request, **kwargs):
        return super(GoogleGatherImport, self).get(request, self.template_name, self.url_suffix, **kwargs)


class GoogleGatherIndex(ObjectIndex):
    url_suffix = '/integration/google/setup/'
    template_name = "gather/google/google_dashboard.html"

    def get(self, request, **kwargs):
        return super(GoogleGatherIndex, self).get(request, self.template_name, self.url_suffix, **kwargs)
