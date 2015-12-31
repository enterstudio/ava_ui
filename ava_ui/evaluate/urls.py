from django.conf.urls import url

from .views import *

urlpatterns = [
    url(r'^template/$', EvaluateTemplateIndex.as_view(),
        name="evaluate-template-index"),

    url(r'^template/new/$', EvaluateTemplateCreate.as_view(),
        name="evaluate-template-create"),

    url(r'^template/(?P<pk>[0-9]+)/$', EvaluateTemplateDetail.as_view(),
        name="evaluate-template-detail"),

    url(r'^results/$', EvaluateResultIndex.as_view(),
        name="evaluate-results-index"),

    # TODO REMOVED DUE TO TIME CONSTRAINTS - WORKS BUT TEMPLATE.HTML NEEDS LOVE
    # url(r'^results/(?P<pk>[0-9]+)/$', EvaluateResultDetail.as_view(),
    #     name="evaluate-results-detail"),
    
    url(r'^sender/$', EvaluateSenderIndex.as_view(),
        name="evaluate-sender-index"),

    url(r'^sender/new/$', EvaluateSenderCreate.as_view(),
        name="evaluate-sender-create"),

    url(r'^sender/(?P<pk>[0-9]+)/$', EvaluateSenderDetail.as_view(),
        name="evaluate-sender-detail"),
    
    url(r'^controller/$', EvaluateControllerIndex.as_view(),
        name="evaluate-controller-index"),

    # TODO relationships during creation
    # url(r'^controller/new/$', EvaluateControllerCreate.as_view(),
    #     name="evaluate-controller-create"),

    url(r'^controller/(?P<pk>[0-9]+)/$', EvaluateControllerDetail.as_view(),
        name="evaluate-controller-detail"),
]
