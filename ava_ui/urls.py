from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [

    url(r'^organize/', include('ava_ui.organize.urls')),
    url(r'^my/', include('ava_ui.my.urls')),
    url(r'^game/', include('ava_ui.game.urls')),
    url(r'^learn/', include('ava_ui.learn.urls')),
    url(r'^test/', include('ava_ui.evaluate.urls')),
    #
    url(r'^/', include('ava_ui.dashboards.urls')),
    #
    url(r'^gather/', include('ava_ui.gather.gather_google.urls')),
    url(r'^gather/', include('ava_ui.gather.gather_ldap.urls')),
    url(r'^integration/', include('ava_ui.integration.integration_google.urls')),
    url(r'^integration/', include('ava_ui.integration.integration_ldap.urls')),

    url(r'^accounts/', include('ava_ui.accounts.urls')),

    # Admin screens
    url(r'^admin/', include(admin.site.urls)),
]
