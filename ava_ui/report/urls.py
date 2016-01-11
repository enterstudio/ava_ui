from django.conf.urls import url

from .views import *

urlpatterns = [
    url(r'^question/$', QuestionIndex.as_view(),
        name="report-question-index"),

    url(r'^question/new/$', QuestionCreate.as_view(),
        name="report-question-create"),

    url(r'^question/(?P<pk>[0-9]+)/$', QuestionDetail.as_view(),
        name="report-question-detail"),

    url(r'^question/update/(?P<pk>[0-9]+)/$', QuestionUpdate.as_view(),
        name="report-question-update"),

    url(r'^question/delete/(?P<pk>[0-9]+)/$', QuestionDelete.as_view(),
        name="report-question-delete"),

    url(r'^suspicious/$', SuspiciousIndex.as_view(),
        name="report-suspicious-index"),

    url(r'^suspicious/new/$', SuspiciousCreate.as_view(),
        name="report-suspicious-create"),

    url(r'^suspicious/(?P<pk>[0-9]+)/$', SuspiciousDetail.as_view(),
        name="report-suspicious-detail"),

    url(r'^suspicious/update/(?P<pk>[0-9]+)/$', SuspiciousUpdate.as_view(),
        name="report-suspicious-update"),

    url(r'^suspicious/delete/(?P<pk>[0-9]+)/$', SuspiciousDelete.as_view(),
        name="report-suspicious-delete"),

    url(r'^response/new/$', ResponseCreate.as_view(),
        name="report-response-create"),

    url(r'^response/update/(?P<pk>[0-9]+)/$', ResponseUpdate.as_view(),
        name="report-response-update"),

    url(r'^response/delete/(?P<pk>[0-9]+)/$', ResponseDelete.as_view(),
        name="report-response-delete"),

]
