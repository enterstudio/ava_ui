from django.conf.urls import url

from .views import PersonIndex, PersonDetail

urlpatterns = [
    url(r'^people/', PersonIndex.as_view(template_name="organize/person/person_index.html"),
        name="person-index"),
    url(r'^people/(?P<pk>\d+)/', PersonDetail.as_view(template_name="organize/person/person_detail.html"),
        name="person-detail"),
]
