from django.conf.urls import url

from .views import PersonIndex, PersonDetail, GroupDetail, GroupIndex

urlpatterns = [
    url(r'^people/$', PersonIndex.as_view(template_name="organize/person/person_index.html"),
        name="person-index"),

    url(r'^people/(?P<pk>[0-9]+)/$', PersonDetail.as_view(template_name="organize/person/person_detail.html"),
        name="person-detail"),

    url(r'^groups/$', GroupIndex.as_view(template_name="organize/group/group_index.html"),
        name="group-index"),

    url(r'^groups/(?P<pk>[0-9]+)/$', GroupDetail.as_view(template_name="organize/group/group_detail.html"),
        name="group-detail"),
]
