from django.conf.urls import url

from .views import *

urlpatterns = [
    url(r'^ldap/$', LDAPGatherIndex.as_view(),
        name="gather-ldap-index"),

    url(r'^ldap/(?P<pk>[0-9]+)/$', LDAPGatherImport.as_view(),
        name="gather-ldap-import"),
   
]
