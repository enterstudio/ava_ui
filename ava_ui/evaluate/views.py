import logging

import requests
from django.shortcuts import render
from django.views import generic

log = logging.getLogger(__name__)


class EvaluateTemplateEmailIndex(ObjectIndex):
    url_suffix = '/evaluate/template/email/'
    template_name = "evaluate/template/email_template_index.html"

    def get(self, request):
        return super(EvaluateTemplateEmailIndex, self).get(request, self.template_name, self.url_suffix)


class EvaluateTemplateEmailDetail(ObjectDetail):
    url_suffix = '/evaluate/template/email/'
    template_name = "evaluate/template/email_template_detail.html"

    def get(self, request, **kwargs):
        return super(EvaluateTemplateEmailDetail, self).get(request, self.template_name, self.url_suffix, **kwargs)
    
class EvaluateTemplateSlackIndex(ObjectIndex):
    url_suffix = '/evaluate/template/slack/'
    template_name = "evaluate/template/slack_template_index.html"

    def get(self, request):
        return super(EvaluateTemplateSlackIndex, self).get(request, self.template_name, self.url_suffix)


class EvaluateTemplateSlackDetail(ObjectDetail):
    url_suffix = '/evaluate/template/slack/'
    template_name = "evaluate/template/slack_template_detail.html"

    def get(self, request, **kwargs):
        return super(EvaluateTemplateSlackDetail, self).get(request, self.template_name, self.url_suffix, **kwargs)