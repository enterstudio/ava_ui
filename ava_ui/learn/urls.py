from django.conf.urls import url

from .views import *

urlpatterns = [
    url(r'^module/$', ModuleIndex.as_view(),
        name="learn-module-index"),

    url(r'^module/new/$', ModuleCreate.as_view(),
        name="learn-module-create"),

    url(r'^module/delete/(?P<pk>[0-9]+)/$', ModuleDelete.as_view(),
        name="learn-module-delete"),
    
    url(r'^module/update/(?P<pk>[0-9]+)/$', ModuleUpdate.as_view(),
        name="learn-module-update"),

    url(r'^module/(?P<pk>[0-9]+)/$', ModuleDetail.as_view(),
        name="learn-module-detail"),
    
    url(r'^role/$', RoleIndex.as_view(),
        name="learn-role-index"),

    url(r'^role/new/$', RoleCreate.as_view(),
        name="learn-role-create"),

    url(r'^role/(?P<pk>[0-9]+)/$', RoleDetail.as_view(),
        name="learn-role-detail"),

    url(r'^role/delete/(?P<pk>[0-9]+)/$', RoleDelete.as_view(),
        name="learn-role-delete"),
    
    url(r'^role/update/(?P<pk>[0-9]+)/$', RoleUpdate.as_view(),
        name="learn-role-update"),
    
    # url(r'^path/update/(?P<pk>[0-9]+)/$', PathUpdate.as_view(),
    #     name="learn-path-update"),

    url(r'^path/$', PathIndex.as_view(),
        name="learn-path-index"),

    url(r'^path/new/$', PathCreate.as_view(),
        name="learn-path-create"),

    url(r'^path/(?P<pk>[0-9]+)/$', PathDetail.as_view(),
        name="learn-path-detail"),

    url(r'^path/delete/(?P<pk>[0-9]+)/$', PathDelete.as_view(),
        name="learn-path-delete"),
]
