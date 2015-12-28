import logging

from ava_ui.abstract.views import ObjectIndex, ObjectDetail

log = logging.getLogger(__name__)


class PersonIndex(ObjectIndex):
    url_suffix = '/organize/person/'
    template_name = "organize/person/person_index.html"

    def get(self, request):
        return super(PersonIndex, self).get(request, self.template_name, self.url_suffix)


class PersonDetail(ObjectDetail):
    url_suffix = '/organize/person/'
    template_name = "organize/person/person_detail.html"

    def get(self, request, **kwargs):
        return super(PersonDetail, self).get(request, self.template_name, self.url_suffix, **kwargs)
