from django.conf.urls import url

from ava_ui.accounts import views

urlpatterns = [
    # Standard authentication functions
    url(r'^login/$', views.login, name='login'),

    url(r'^logout/$', views.logout, name='logout'),

    url(r'^password/reset/$', views.password_reset, name='password-reset'),

    url(r'^password/reset/confirm/$', views.password_reset_confirm, name='password-reset-confirm'),

    url(r'^password/reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        views.password_reset_confirm, name='password-reset-confirm-token'),

    url(r'^password/reset/done/$', views.password_reset_done, name='password-reset-done'),

    url(r'^password/reset/complete/$', views.password_reset_complete, name='password-reset-complete'),

    # TODO Authentication and permissions for this
    url(r'^password/change/$', views.password_change, name='password-change'),

    # TODO Authentication and permissions for this
    url(r'^password/change/done/$', views.password_change_done, name='password-change-done'),

]
