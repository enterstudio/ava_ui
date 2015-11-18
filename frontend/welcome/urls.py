from ava.utils import require_ava_superuser
from django.conf.urls import patterns, url

from . import views


urlpatterns = patterns(
    '',
    url('^first-user/$', views.CreateFirstUser.as_view(), name='welcome-first-user'),
    url('^importer-selection/$', require_ava_superuser(views.ImportSelection.as_view()), name='welcome-importer-selection'),
    url('^importer-ldap/$', require_ava_superuser(views.ImportLDAP.as_view()), name='welcome-importer-ldap'),
    url('^importer-google/$', require_ava_superuser(views.ImportGoogle.as_view()), name='welcome-importer-google'),
    url('^importer-progress/$', require_ava_superuser(views.ImportProgress.as_view()), name='welcome-importer-progress'),
)
