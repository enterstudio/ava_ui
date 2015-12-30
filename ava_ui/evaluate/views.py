import logging

from ava_ui.abstract.views import ObjectCreate, ObjectDetail, ObjectIndex

log = logging.getLogger(__name__)


class EvaluateTemplateEmailIndex(ObjectIndex):
    url_suffix = '/evaluate/template_email/'
    template_name = "evaluate/template_email/email_template_index.html"

    def get(self, request):
        return super(EvaluateTemplateEmailIndex, self).get(request, self.template_name, self.url_suffix)


class EvaluateTemplateEmailDetail(ObjectDetail):
    url_suffix = '/evaluate/template_email/'
    template_name = "evaluate/template_email/email_template_detail.html"

    def get(self, request, **kwargs):
        return super(EvaluateTemplateEmailDetail, self).get(request, self.template_name, self.url_suffix, **kwargs)


class EvaluateTemplateEmailCreate(ObjectCreate):
    url_suffix = '/evaluate/template_email/'
    template_name = "evaluate/template_email/email_template_form.html"

    def get(self, request):
        return super(EvaluateTemplateEmailIndex, self).get(request, self.template_name, self.url_suffix)

    def post(self, request, **kwargs):
        expected_fields = ['name', 'description', 'subject', 'body']
        redirect_url = 'evaluate-template-email-list'
        return super(EvaluateTemplateEmailCreate, self).post(request=request, template_name=self.template_name,
                                                             url_suffix=self.url_suffix,
                                                             expected_fields=expected_fields,
                                                             redirect_url=redirect_url,
                                                             **kwargs)


class EvaluateTemplateSlackIndex(ObjectIndex):
    url_suffix = '/evaluate/template_slack/'
    template_name = "evaluate/template/slack_template_index.html"

    def get(self, request):
        return super(EvaluateTemplateSlackIndex, self).get(request, self.template_name, self.url_suffix)


class EvaluateTemplateSlackDetail(ObjectDetail):
    url_suffix = '/evaluate/template_slack/'
    template_name = "evaluate/template/slack_template_detail.html"

    def get(self, request, **kwargs):
        return super(EvaluateTemplateSlackDetail, self).get(request, self.template_name, self.url_suffix, **kwargs)


class EvaluateTemplateSlackCreate(ObjectCreate):
    url_suffix = '/evaluate/template_slack/'
    template_name = "evaluate/template_slack/slack_template_form.html"

    def get(self, request):
        return super(EvaluateTemplateSlackIndex, self).get(request, self.template_name, self.url_suffix)

    def post(self, request, **kwargs):
        expected_fields = ['name', 'description']
        redirect_url = 'evaluate-template-slack-list'
        return super(EvaluateTemplateSlackCreate, self).post(request=request, template_name=self.template_name,
                                                             url_suffix=self.url_suffix,
                                                             expected_fields=expected_fields,
                                                             redirect_url=redirect_url,
                                                             **kwargs)

class EvaluateResultIndex(ObjectIndex):
    url_suffix = '/evaluate/result/'
    template_name = "evaluate/results/evaluate_result_index.html"

    def get(self, request):
        return super(EvaluateResultIndex, self).get(request, self.template_name, self.url_suffix)


# TODO REMOVED DUE TO TIME CONSTRAINTS - WORKS BUT TEMPLATE.HTML NEEDS LOVE
# class EvaluateResultDetail(ObjectDetail):
#     url_suffix = '/evaluate/result/'
#     template_name = "evaluate/results/evaluate_result_detail.html"
#
#     def get(self, request, **kwargs):
#         return super(EvaluateResultDetail, self).get(request, self.template_name, self.url_suffix, **kwargs)