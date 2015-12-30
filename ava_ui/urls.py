from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [

    url(r'^organize/', include('ava_ui.organize.urls')),
    url(r'^my/', include('ava_ui.my.urls')),
    # url(r'^game/', include('ava_ui.game.urls')),
    # url(r'^learn/', include('ava_ui.learn.urls')),
    url(r'^evaluate/', include('ava_ui.evaluate.urls')),
    #
    # url(r'^notify/', include('ava_ui.notify.urls')),
    #
    # url(r'^gather/google/', include('ava_ui.gather.gather_google.urls')),
    # url(r'^gather/ldap/', include('ava_ui.gather.gather_ldap.urls')),
    # url(r'^integration/google/', include('ava_ui.integration.integration_google.urls')),
    # url(r'^integration/ldap/', include('ava_ui.integration.integration_ldap.urls')),

    url(r'^accounts/', include('ava_ui.accounts.urls')),
    # url(r'^accounts/registration/', include('ava_ui.accounts.registration.urls')),

    # Admin screens
    url(r'^admin/', include(admin.site.urls)),
]
