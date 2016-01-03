from django.conf.urls import url

from .views import *

urlpatterns = [
    url(r'^google/$', GoogleIntegrationIndex.as_view(),
        name="integration-google-index"),

    url(r'^google/new/$', GoogleIntegrationCreate.as_view(),
        name="integration-google-create"),

    url(r'^google/(?P<pk>[0-9]+)/$', GoogleIntegrationDetail.as_view(),
        name="integration-google-detail"),

    url(r'^google/delete/(?P<pk>[0-9]+)/$', GoogleIntegrationDelete.as_view(),
        name="integration-google-delete"),

    url(r'^google/auth/(?P<pk>[0-9]+)/$',  GoogleIntegrationAuthorize.as_view(),
        name="integration-google-auth"),

   url(r'^google/callback/',  GoogleIntegrationAuthorizeCallback.as_view(),
        name="integration-google-callback"),
]
