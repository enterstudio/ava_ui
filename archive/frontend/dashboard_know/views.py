# flake8: noqa

from django.shortcuts import get_object_or_404
from django.views import generic
from ava.core_group.models import Group
from ava.core_identity.models import Person, Identity
from ava.import_google.models import GoogleConfiguration
from ava.import_google.stats_interface import GoogleStatistics
from ava.import_ldap.models import LDAPConfiguration
from ava.import_ldap.stats_interface import LDAPStatistics


class KnowDashboardView(generic.ListView):
    template_name = 'know/dashboard.html'
    model = LDAPConfiguration
    context_object_name = 'list'

    def get_context_data(self, **kwargs):
        context = super(KnowDashboardView, self).get_context_data(**kwargs)
        context['ldap_config'] = LDAPConfiguration.objects.all()
        context['google_config'] = GoogleConfiguration.objects.all()
        context['ldap'] = LDAPStatistics().get_all_stats()
        context['google'] = GoogleStatistics().get_all_stats()
        context['person_count'] = Person.objects.count()
        context['identity_count'] = Identity.objects.count()
        context['group_count'] = Group.objects.count()
        return context


class KnowLDAPDashboardView(generic.ListView):
    template_name = 'know/ldap_dashboard.html'
    model = LDAPConfiguration
    context_object_name = 'list'

    def get_context_data(self, **kwargs):
        context = super(KnowLDAPDashboardView, self).get_context_data(**kwargs)
        pk = self.kwargs.get('pk')
        if pk:
            ldap_config = get_object_or_404(LDAPConfiguration, pk=pk)
            context['ldap'] = LDAPStatistics().get_stats(ldap_config)
        else:
            context['ldap'] = LDAPStatistics().get_all_stats()

        context['person_count'] = Person.objects.count()
        context['identity_count'] = Identity.objects.count()
        context['group_count'] = Group.objects.count()
        return context


class KnowGoogleDashboardView(generic.ListView):
    template_name = 'know/google_dashboard.html'
    model = GoogleConfiguration
    context_object_name = 'list'

    def get_context_data(self, **kwargs):
        context = super(KnowGoogleDashboardView, self).get_context_data(**kwargs)
        pk = self.kwargs.get('pk')
        if pk:
            google_config = get_object_or_404(GoogleConfiguration, pk=pk)
            context['google'] = GoogleStatistics().get_stats(google_config)
        else:
            context['google'] = GoogleStatistics().get_all_stats()

        context['person_count'] = Person.objects.count()
        context['identity_count'] = Identity.objects.count()
        context['group_count'] = Group.objects.count()
        return context
