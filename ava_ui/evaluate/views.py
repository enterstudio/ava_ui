import logging

from ava_ui.abstract.views import ObjectCreate, ObjectDetail, ObjectIndex

log = logging.getLogger(__name__)


class EvaluateTemplateIndex(ObjectIndex):
    url_suffix = '/evaluate/template/'
    template_name = "evaluate/template/template_index.html"

    def get(self, request):
        return super(EvaluateTemplateIndex, self).get(request, self.template_name, self.url_suffix)


class EvaluateTemplateDetail(ObjectDetail):
    url_suffix = '/evaluate/template/'
    template_name = "evaluate/template/template_detail.html"

    def get(self, request, **kwargs):
        return super(EvaluateTemplateDetail, self).get(request, self.template_name, self.url_suffix, **kwargs)


class EvaluateTemplateCreate(ObjectCreate):
    url_suffix = '/evaluate/template/'
    template_name = "evaluate/template/template_form.html"

    def get(self, request):
        return super(EvaluateTemplateIndex, self).get(request, self.template_name, self.url_suffix)

    def post(self, request, **kwargs):
        expected_fields = ['name', 'description', 'template_type', 'email_subject', 'email_body']
        redirect_url = 'evaluate-template-list'
        return super(EvaluateTemplateCreate, self).post(request=request, template_name=self.template_name,
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

class EvaluateSenderIndex(ObjectIndex):
    url_suffix = '/evaluate/sender/'
    sender_name = "evaluate/sender/sender_index.html"

    def get(self, request):
        return super(EvaluateSenderIndex, self).get(request, self.sender_name, self.url_suffix)


class EvaluateSenderDetail(ObjectDetail):
    url_suffix = '/evaluate/sender/'
    sender_name = "evaluate/sender/sender_detail.html"

    def get(self, request, **kwargs):
        return super(EvaluateSenderDetail, self).get(request, self.sender_name, self.url_suffix, **kwargs)


class EvaluateSenderCreate(ObjectCreate):
    url_suffix = '/evaluate/sender/'
    sender_name = "evaluate/sender/sender_form.html"

    def get(self, request):
        return super(EvaluateSenderIndex, self).get(request, self.sender_name, self.url_suffix)

    def post(self, request, **kwargs):
        expected_fields = ['first_name', 'last_name', 'email_address', 'slack_name']
        redirect_url = 'evaluate-sender-list'
        return super(EvaluateSenderCreate, self).post(request=request, sender_name=self.sender_name,
                                                      url_suffix=self.url_suffix,
                                                      expected_fields=expected_fields,
                                                      redirect_url=redirect_url,
                                                      **kwargs)


class EvaluateControllerIndex(ObjectIndex):
    url_suffix = '/evaluate/controller/'
    controller_name = "evaluate/controller/controller_index.html"

    def get(self, request):
        return super(EvaluateControllerIndex, self).get(request, self.controller_name, self.url_suffix)


class EvaluateControllerDetail(ObjectDetail):
    url_suffix = '/evaluate/controller/'
    controller_name = "evaluate/controller/controller_detail.html"

    def get(self, request, **kwargs):
        return super(EvaluateControllerDetail, self).get(request, self.controller_name, self.url_suffix, **kwargs)

# TODO RELATIONSHIPS WTF HELP
# class EvaluateControllerCreate(ObjectCreate):
#     url_suffix = '/evaluate/controller/'
#     controller_name = "evaluate/controller/controller_form.html"
#
#     def get(self, request):
#         return super(EvaluateControllerIndex, self).get(request, self.controller_name, self.url_suffix)
#
#     def post(self, request, **kwargs):
#         expected_fields = ['scheduled_type', 'scheduled_time', 'expiry_type', 'expiry_time', 'sender', 'template',
#                            'targets',
#                            'status']
#         redirect_url = 'evaluate-controller-list'
#         return super(EvaluateControllerCreate, self).post(request=request, controller_name=self.controller_name,
#                                                           url_suffix=self.url_suffix,
#                                                           expected_fields=expected_fields,
#                                                           redirect_url=redirect_url,
#                                                           **kwargs)

class EvaluateTargetProfileIndex(ObjectIndex):
    url_suffix = '/evaluate/target/'
    target_name = "evaluate/target/target_index.html"

    def get(self, request):
        return super(EvaluateTargetProfileIndex, self).get(request, self.target_name, self.url_suffix)


class EvaluateTargetProfileDetail(ObjectDetail):
    url_suffix = '/evaluate/target/'
    target_name = "evaluate/target/target_detail.html"

    def get(self, request, **kwargs):
        return super(EvaluateTargetProfileDetail, self).get(request, self.target_name, self.url_suffix, **kwargs)

# TODO RELATIONSHIPS WTF HELP
# class EvaluateTargetProfileCreate(ObjectCreate):
#     url_suffix = '/evaluate/target/'
#     target_name = "evaluate/target/target_form.html"
#
#     def get(self, request):
#         return super(EvaluateTargetProfileIndex, self).get(request, self.target_name, self.url_suffix)
#
#     def post(self, request, **kwargs):
#         expected_fields = ['target_controller', 'target', 'token', 'delivery_status']
#         redirect_url = 'evaluate-target-list'
#         return super(EvaluateTargetProfileCreate, self).post(request=request, target_name=self.target_name,
#                                                       url_suffix=self.url_suffix,
#                                                       expected_fields=expected_fields,
#                                                       redirect_url=redirect_url,
#                                                       **kwargs)