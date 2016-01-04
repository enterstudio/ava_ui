import logging

from ava_ui.abstract.views import ObjectCreate, ObjectDetail, ObjectIndex, ObjectDelete, ObjectUpdate

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
        return super(EvaluateTemplateCreate, self).get(request, self.template_name, self.url_suffix)

    def post(self, request, **kwargs):
        expected_fields = ['name', 'description', 'template_type', 'email_subject', 'email_body']
        redirect_url = 'evaluate-template-index'
        return super(EvaluateTemplateCreate, self).post(request=request, template_name=self.template_name,
                                                        url_suffix=self.url_suffix,
                                                        expected_fields=expected_fields,
                                                        redirect_url=redirect_url,
                                                        **kwargs)
class EvaluateTemplateUpdate(ObjectUpdate):
    url_suffix = '/evaluate/template/'
    template_name = "evaluate/template/template_update.html"

    def get(self, request, **kwargs):
        return super(EvaluateTemplateUpdate, self).get(request, self.template_name, self.url_suffix, **kwargs)

    def post(self, request, **kwargs):
        expected_fields = ['name', 'description', 'template_type', 'email_subject', 'email_body']
        redirect_url = 'evaluate-template-index'
        return super(EvaluateTemplateUpdate, self).post(request=request, template_name=self.template_name,
                                                        url_suffix=self.url_suffix,
                                                        expected_fields=expected_fields,
                                                        redirect_url=redirect_url,
                                                        **kwargs)


class EvaluateTemplateDelete(ObjectDelete):
    url_suffix = '/evaluate/template/'
    redirect_url = 'evaluate-template-index'

    def get(self, request, **kwargs):
        return super(EvaluateTemplateDelete, self).get(request=request,
                                                       url_suffix=self.url_suffix,
                                                       redirect_url=self.redirect_url,
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
    template_name = "evaluate/sender/sender_index.html"

    def get(self, request):
        return super(EvaluateSenderIndex, self).get(request, self.template_name, self.url_suffix)


class EvaluateSenderDetail(ObjectDetail):
    url_suffix = '/evaluate/sender/'
    template_name = "evaluate/sender/sender_detail.html"

    def get(self, request, **kwargs):
        return super(EvaluateSenderDetail, self).get(request, self.template_name, self.url_suffix, **kwargs)


class EvaluateSenderCreate(ObjectCreate):
    url_suffix = '/evaluate/sender/'
    template_name = "evaluate/sender/sender_form.html"

    def get(self, request):
        return super(EvaluateSenderCreate, self).get(request, self.template_name, self.url_suffix)

    def post(self, request, **kwargs):
        expected_fields = ['first_name', 'last_name', 'email_address', 'slack_name']
        redirect_url = 'evaluate-sender-index'
        return super(EvaluateSenderCreate, self).post(request=request, template_name=self.template_name,
                                                      url_suffix=self.url_suffix,
                                                      expected_fields=expected_fields,
                                                      redirect_url=redirect_url,
                                                      **kwargs)

class EvaluateSenderUpdate(ObjectUpdate):
    url_suffix = '/evaluate/sender/'
    template_name = "evaluate/sender/sender_update.html"

    def get(self, request, **kwargs):
        return super(EvaluateSenderUpdate, self).get(request, self.template_name, self.url_suffix, **kwargs)

    def post(self, request, **kwargs):
        expected_fields = ['first_name', 'last_name', 'email_address', 'slack_name']
        redirect_url = 'evaluate-sender-index'
        return super(EvaluateSenderUpdate, self).post(request=request, template_name=self.template_name,
                                                      url_suffix=self.url_suffix,
                                                      expected_fields=expected_fields,
                                                      redirect_url=redirect_url,
                                                      **kwargs)

class EvaluateSenderDelete(ObjectDelete):
    url_suffix = '/evaluate/sender/'
    redirect_url = 'evaluate-sender-index'

    def get(self, request, **kwargs):
        return super(EvaluateSenderDelete, self).get(request=request,
                                                     url_suffix=self.url_suffix,
                                                     redirect_url=self.redirect_url,
                                                     **kwargs)


class EvaluateControllerIndex(ObjectIndex):
    url_suffix = '/evaluate/controller/'
    template_name = "evaluate/controller/controller_index.html"

    def get(self, request):
        return super(EvaluateControllerIndex, self).get(request, self.template_name, self.url_suffix)


class EvaluateControllerDetail(ObjectDetail):
    url_suffix = '/evaluate/controller/'
    template_name = "evaluate/controller/controller_detail.html"

    def get(self, request, **kwargs):
        return super(EvaluateControllerDetail, self).get(request, self.template_name, self.url_suffix, **kwargs)


# TODO RELATIONSHIPS WTF HELP
# class EvaluateControllerCreate(ObjectCreate):
#     url_suffix = '/evaluate/controller/'
#     template_name = "evaluate/controller/controller_form.html"
#
#     def get(self, request):
#         return super(EvaluateControllerCreate, self).get(request, self.template_name, self.url_suffix)
#
#     def post(self, request, **kwargs):
#         expected_fields = ['scheduled_type', 'scheduled_time', 'expiry_type', 'expiry_time', 'sender', 'template',
#                            'targets',
#                            'status']
#         redirect_url = 'evaluate-controller-index'
#         return super(EvaluateControllerCreate, self).post(request=request, template_name=self.template_name,
#                                                           url_suffix=self.url_suffix,
#                                                           expected_fields=expected_fields,
#                                                           redirect_url=redirect_url,
#                                                           **kwargs)

# TODO RELATIONSHIPS WTF HELP
# class EvaluateControllerUpdate(ObjectUpdate):
#     url_suffix = '/evaluate/controller/'
#     template_name = "evaluate/controller/controller_update.html"
#
#     def get(self, request, **kwargs):
#         return super(EvaluateControllerUpdate, self).get(request, self.template_name, self.url_suffix, **kwargs)
#
#     def post(self, request, **kwargs):
#         expected_fields = ['scheduled_type', 'scheduled_time', 'expiry_type', 'expiry_time', 'sender', 'template',
#                            'targets',
#                            'status']
#         redirect_url = 'evaluate-controller-index'
#         return super(EvaluateControllerUpdate, self).post(request=request, template_name=self.template_name,
#                                                           url_suffix=self.url_suffix,
#                                                           expected_fields=expected_fields,
#                                                           redirect_url=redirect_url,
# 

class EvaluateControllerDelete(ObjectDelete):
    url_suffix = '/evaluate/controller/'
    redirect_url = 'evaluate-controller-index'

    def get(self, request, **kwargs):
        return super(EvaluateControllerDelete, self).get(request=request,
                                                         url_suffix=self.url_suffix,
                                                         redirect_url=self.redirect_url,
                                                         **kwargs)


class EvaluateTargetProfileIndex(ObjectIndex):
    url_suffix = '/evaluate/target/'
    template_name = "evaluate/target/target_index.html"

    def get(self, request):
        return super(EvaluateTargetProfileIndex, self).get(request, self.template_name, self.url_suffix)


class EvaluateTargetProfileDetail(ObjectDetail):
    url_suffix = '/evaluate/target/'
    template_name = "evaluate/target/target_detail.html"

    def get(self, request, **kwargs):
        return super(EvaluateTargetProfileDetail, self).get(request, self.template_name, self.url_suffix, **kwargs)

# TODO RELATIONSHIPS WTF HELP
# class EvaluateTargetProfileCreate(ObjectCreate):
#     url_suffix = '/evaluate/target/'
#     template_name = "evaluate/target/target_form.html"
#
#     def get(self, request):
#         return super(EvaluateTargetProfileCreate, self).get(request, self.template_name, self.url_suffix)
#
#     def post(self, request, **kwargs):
#         expected_fields = ['target_controller', 'target', 'token', 'delivery_status']
#         redirect_url = 'evaluate-target-index'
#         return super(EvaluateTargetProfileCreate, self).post(request=request, template_name=self.template_name,
#                                                       url_suffix=self.url_suffix,
#                                                       expected_fields=expected_fields,
#                                                       redirect_url=redirect_url,
#                                                       **kwargs)

# TODO RELATIONSHIPS WTF HELP
# class EvaluateTargetProfileUpdate(ObjectUpdate):
#     url_suffix = '/evaluate/target/'
#     template_name = "evaluate/target/target_update.html"
#
#     def get(self, request, **kwargs):
#         return super(EvaluateTargetProfileUpdate, self).get(request, self.template_name, self.url_suffix, **kwargs)
#
#     def post(self, request, **kwargs):
#         expected_fields = ['target_controller', 'target', 'token', 'delivery_status']
#         redirect_url = 'evaluate-target-index'
#         return super(EvaluateTargetProfileUpdate, self).post(request=request, template_name=self.template_name,
#                                                       url_suffix=self.url_suffix,
#                                                       expected_fields=expected_fields,
#                                                       redirect_url=redirect_url,
#   


class EvaluateTargetProfileDelete(ObjectDelete):
    url_suffix = '/evaluate/target/'
    redirect_url = 'evaluate-target-index'

    def get(self, request, **kwargs):
        return super(EvaluateTargetProfileDelete, self).get(request=request,
                                                            url_suffix=self.url_suffix,
                                                            redirect_url=self.redirect_url,
                                                            **kwargs)
