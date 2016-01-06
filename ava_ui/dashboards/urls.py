from django.conf.urls import url

from .views import *

urlpatterns = [
    url(r'^educate/dashboard/$', EducateDashboard.as_view(),
        name="educate-index"),

    url(r'^test/dashboard/$', TestDashboard.as_view(),
        name="test-index"),

    url(r'^know/dashboard/$', KnowDashboard.as_view(),
        name="know-index"),
]
