import logging

from ava_ui.abstract.views import ObjectDashboard

log = logging.getLogger(__name__)


class EducateDashboard(ObjectDashboard):
    url_suffix = ''
    template_name = "learn/index.html"

    def get(self, request):
        return super(EducateDashboard, self).get(request, self.template_name, self.url_suffix)


class TestDashboard(ObjectDashboard):
    url_suffix = ''
    template_name = "evaluate/index.html"

    def get(self, request):
        return super(TestDashboard, self).get(request, self.template_name, self.url_suffix)


class KnowDashboard(ObjectDashboard):
    url_suffix = ''
    template_name = "organize/index.html"

    def get(self, request):
        return super(KnowDashboard, self).get(request, self.template_name, self.url_suffix)
