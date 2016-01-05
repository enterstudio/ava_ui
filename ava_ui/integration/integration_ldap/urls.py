from django.conf.urls import url

from .views import *

urlpatterns = [
    url(r'^ldap/$', LDAPIntegrationIndex.as_view(),
        name="integration-ldap-index"),

    url(r'^ldap/new/$', LDAPIntegrationCreate.as_view(),
        name="integration-ldap-create"),

    url(r'^ldap/(?P<pk>[0-9]+)/$', LDAPIntegrationDetail.as_view(),
        name="integration-ldap-detail"),

    url(r'^ldap/delete/(?P<pk>[0-9]+)/$', LDAPIntegrationDelete.as_view(),
        name="integration-ldap-delete"),

    url(r'^ldap/update/(?P<pk>[0-9]+)/$', LDAPIntegrationUpdate.as_view(),
        name="integration-ldap-update"),
   
]
