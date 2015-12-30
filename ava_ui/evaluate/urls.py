from django.conf.urls import url

from .views import *

urlpatterns = [
    url(r'^template/email/$', EvaluateTemplateEmailIndex.as_view(),
        name="evaluate-template-email-index"),

    url(r'^template/email/new/$', EvaluateTemplateEmailCreate.as_view(),
        name="evaluate-template-email-create"),

    url(r'^template/email/(?P<pk>[0-9]+)/$', EvaluateTemplateEmailDetail.as_view(),
        name="evaluate-template-email-detail"),

    url(r'^template/slack/$', EvaluateTemplateSlackIndex.as_view(),
        name="evaluate-template-slack-index"),

    url(r'^template/slack/new/$', EvaluateTemplateSlackCreate.as_view(),
        name="evaluate-template-slack-create"),

    url(r'^template/slack/(?P<pk>[0-9]+)/$', EvaluateTemplateSlackDetail.as_view(),
        name="evaluate-template-slack-detail"),

    url(r'^results/$', EvaluateResultIndex.as_view(),
        name="evaluate-results-index"),

    # TODO REMOVED DUE TO TIME CONSTRAINTS - WORKS BUT TEMPLATE.HTML NEEDS LOVE
    # url(r'^results/(?P<pk>[0-9]+)/$', EvaluateResultDetail.as_view(),
    #     name="evaluate-results-detail"),
]
