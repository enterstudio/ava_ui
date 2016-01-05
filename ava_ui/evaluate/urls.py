from django.conf.urls import url

from .views import *

urlpatterns = [
    url(r'^template/$', EvaluateTemplateIndex.as_view(),
        name="evaluate-template-index"),

    url(r'^template/new/$', EvaluateTemplateCreate.as_view(),
        name="evaluate-template-create"),

    url(r'^template/(?P<pk>[0-9]+)/$', EvaluateTemplateDetail.as_view(),
        name="evaluate-template-detail"),

    url(r'^template/update/(?P<pk>[0-9]+)/$', EvaluateTemplateUpdate.as_view(),
        name="evaluate-template-update"),

    url(r'^template/delete/(?P<pk>[0-9]+)/$', EvaluateTemplateDelete.as_view(),
        name="evaluate-template-delete"),

    url(r'^results/$', EvaluateResultIndex.as_view(),
        name="evaluate-results-index"),

    url(r'^sender/$', EvaluateSenderIndex.as_view(),
        name="evaluate-sender-index"),

    url(r'^sender/new/$', EvaluateSenderCreate.as_view(),
        name="evaluate-sender-create"),

    url(r'^sender/(?P<pk>[0-9]+)/$', EvaluateSenderDetail.as_view(),
        name="evaluate-sender-detail"),

    url(r'^sender/delete/(?P<pk>[0-9]+)/$', EvaluateSenderDelete.as_view(),
        name="evaluate-sender-delete"),

    url(r'^sender/update/(?P<pk>[0-9]+)/$', EvaluateSenderUpdate.as_view(),
        name="evaluate-sender-update"),

    url(r'^controller/$', EvaluateControllerIndex.as_view(),
        name="evaluate-controller-index"),

    url(r'^controller/new/$', EvaluateControllerCreate.as_view(),
        name="evaluate-controller-create"),

    url(r'^controller/(?P<pk>[0-9]+)/$', EvaluateControllerDetail.as_view(),
        name="evaluate-controller-detail"),

    url(r'^controller/update/(?P<pk>[0-9]+)/$', EvaluateControllerUpdate.as_view(),
        name="evaluate-controller-update"),

    url(r'^target/$', EvaluateTargetProfileIndex.as_view(),
        name="evaluate-target-index"),

    url(r'^target/(?P<pk>[0-9]+)/$', EvaluateTargetProfileDetail.as_view(),
        name="evaluate-target-detail"),




]
