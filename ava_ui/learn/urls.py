from django.conf.urls import url

from .views import *

urlpatterns = [
    url(r'^learn/module/$', ModuleIndex.as_view(),
        name="learn-module-index"),

    url(r'^learn/module/new/$', ModuleCreate.as_view(),
        name="learn-module-create"),

    url(r'^learn/module/(?P<pk>[0-9]+)/$', ModuleDetail.as_view(),
        name="learn-module-detail"),
    
    url(r'^learn/role/$', RoleIndex.as_view(),
        name="learn-role-index"),

    url(r'^learn/role/new/$', RoleCreate.as_view(),
        name="learn-role-create"),

    url(r'^learn/role/(?P<pk>[0-9]+)/$', RoleDetail.as_view(),
        name="learn-role-detail"),
    
    url(r'^learn/path/$', PathIndex.as_view(),
        name="learn-path-index"),

    url(r'^learn/path/new/$', PathCreate.as_view(),
        name="learn-path-create"),

    url(r'^learn/path/(?P<pk>[0-9]+)/$', PathDetail.as_view(),
        name="learn-path-detail"),
]
