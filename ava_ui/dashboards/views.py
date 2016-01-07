import logging

from django.conf import settings
from django.contrib.auth import load_backend
from django.contrib.auth.models import AnonymousUser

from ava_ui.abstract.views import ObjectDashboard

log = logging.getLogger(__name__)


class EducateDashboard(ObjectDashboard):
    url_suffix = ''
    template_name = "dashboards/educate_index.html"

    def get(self, request):
        return super(EducateDashboard, self).get(request, self.template_name, self.url_suffix)


class TestDashboard(ObjectDashboard):
    url_suffix = ''
    template_name = "dashboards/test_index.html"

    def get(self, request):
        return super(TestDashboard, self).get(request, self.template_name, self.url_suffix)


class KnowDashboard(ObjectDashboard):
    url_suffix = ''
    template_name = "dashboards/know_index.html"

    def get(self, request):
        return super(KnowDashboard, self).get(request, self.template_name, self.url_suffix)

class MyDashboard(ObjectDashboard):
    url_suffix = ''
    template_name = "dashboards/my_index.html"

    def get(self, request):
        return super(MyDashboard, self).get(request, self.template_name, self.url_suffix)


class GatherDashboard(ObjectDashboard):
    url_suffix = ''
    template_name = "dashboards/gather_index.html"

    def get(self, request):
        return super(GatherDashboard, self).get(request, self.template_name, self.url_suffix)


class IntegrationDashboard(ObjectDashboard):
    url_suffix = ''
    template_name = "dashboards/integration_index.html"

    def get(self, request):
        return super(IntegrationDashboard, self).get(request, self.template_name, self.url_suffix)

class  GameDashboard(ObjectDashboard):
    url_suffix = ''
    template_name = "dashboards/game_index.html"

    def get(self, request):
        return super(GameDashboard, self).get(request, self.template_name, self.url_suffix)

class EvaluateDashboard(ObjectDashboard):
    url_suffix = ''
    template_name = "dashboards/evaluate_index.html"

    def get(self, request):
        return super(EvaluateDashboard, self).get(request, self.template_name, self.url_suffix)

class LearnDashboard(ObjectDashboard):
    url_suffix = ''
    template_name = "dashboards/learn_index.html"

    def get(self, request):
        return super(LearnDashboard, self).get(request, self.template_name, self.url_suffix)

class OrganizeDashboard(ObjectDashboard):
    url_suffix = ''
    template_name = "dashboards/organize_index.html"

    def get(self, request):
        return super(OrganizeDashboard, self).get(request, self.template_name, self.url_suffix)

class UserDashboard(ObjectDashboard):
    url_suffix = ''
    template_name = "dashboards/user_index.html"

    def get(self, request):
        return super(UserDashboard, self).get(request, self.template_name, self.url_suffix)

class ManagerDashboard(ObjectDashboard):
    url_suffix = ''
    template_name = "dashboards/manager_index.html"

    def get(self, request):
        return super(ManagerDashboard, self).get(request, self.template_name, self.url_suffix)