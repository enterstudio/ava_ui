from django.conf.urls import patterns, url
from django.contrib.auth.decorators import login_required

from ava.dashboard_know import views

urlpatterns = patterns(
    '',
    url(r'^$', login_required(views.KnowDashboardView.as_view()), name='know-dashboard'),
    url('^(?P<pk>\d+)/ldap/$', login_required(views.KnowLDAPDashboardView.as_view()), name='know-no-ldap-dashboard'),
    url('^(?P<pk>\d+)/google/$', login_required(views.KnowGoogleDashboardView.as_view()),
        name='know-no-google-dashboard'),
    url('^ldap/$', login_required(views.KnowLDAPDashboardView.as_view()), name='know-ldap-dashboard'),
    url('^google/$', login_required(views.KnowGoogleDashboardView.as_view()),
        name='know-google-dashboard'),
)
