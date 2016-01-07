from django.conf.urls import url

from .views import *

urlpatterns = [

    url(r'^know/dashboard/$', OrganizeDashboard.as_view(),
        name="know-index"),

    url(r'^learn/dashboard/$', LearnDashboard.as_view(),
        name="educate-index"),

    url(r'^evaluate/dashboard/$', EvaluateDashboard.as_view(),
        name="evaluate-index"),

    url(r'^my/dashboard/$', MyDashboard.as_view(),
        name="my-index"),

    url(r'^game/dashboard/$', GameDashboard.as_view(),
        name="game-index"),

    url(r'^organize/dashboard/$', OrganizeDashboard.as_view(),
        name="organize-index"),

    url(r'^gather/dashboard/$', GatherDashboard.as_view(),
        name="gather-index"),

    url(r'^integration/dashboard/$', IntegrationDashboard.as_view(),
        name="integration-index"),

    url(r'^manager/dashboard/$', ManagerDashboard.as_view(),
        name="manager-index"),

    url(r'^user/dashboard/$', UserDashboard.as_view(),
        name="user-index"),
]
