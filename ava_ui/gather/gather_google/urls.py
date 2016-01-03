from django.conf.urls import url

from .views import *

urlpatterns = [
    url(r'^google/$', GoogleGatherIndex.as_view(),
        name="gather-google-index"),

    url(r'^google/(?P<pk>[0-9]+)/$', GoogleGatherImport.as_view(),
        name="gather-google-import"),
   
]
