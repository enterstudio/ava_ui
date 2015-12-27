from django.conf.urls import url
from ava_ui.accounts import views

# from ava_ui.accounts.decorators import system_admin_required

urlpatterns = [
    # Standard authentication functions
    url(r'^login/$', views.login, name='login'),

    url(r'^logout/$', views.logout, name='logout'),

    url(
        '^password_change/',
        'django.contrib.auth.views.password_change',
        {'template_name': 'accounts/password-change.html'},
        name='password_change'
    ),

    url(
        '^password_change/done/',
        'django.contrib.auth.views.password_change_done',
        {'template_name': 'accounts/password-change-done.html'},
        name='password_change_done'
    ),
    url(
        '^password_reset/$',
        'django.contrib.auth.views.password_reset',
        {'template_name': 'accounts/password-reset.html'},
        name='password_reset'
    ),
    url(
        '^password_reset/done/$',
        'django.contrib.auth.views.password_reset_done',
        {'template_name': 'accounts/password-reset-done.html', 'post_reset_redirect': '/'},
        name='password_reset_done'
    ),
    url(
        '^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        'django.contrib.auth.views.password_reset_confirm',
        {'template_name': 'accounts/password-reset-confirm.html'},
        name='password_reset_confirm'
    ),
    url(
        '^reset/done/',
        'django.contrib.auth.views.password_reset_complete',
        {'template_name': 'accounts/password-reset-complete.html'},
        name='password_reset_complete'
    ),

]
