import logging

from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

from ava_ui.abstract.views import ObjectIndex, ObjectDetail, ObjectCreate, ObjectDelete, ObjectUpdate

log = logging.getLogger(__name__)


class QuestionIndex(LoginRequiredMixin, PermissionRequiredMixin, ObjectIndex):
    permission_required = 'is_staff'
    url_suffix = '/report/question/'
    template_name = "report/question/question_index.html"

    def get(self, request):
        return super(QuestionIndex, self).get(request, self.template_name, self.url_suffix)


class QuestionDetail(LoginRequiredMixin, PermissionRequiredMixin, ObjectDetail):
    permission_required = 'is_staff'
    url_suffix = '/report/question/'
    template_name = "report/question/question_detail.html"

    def get(self, request, **kwargs):
        return super(QuestionDetail, self).get(request, self.template_name, self.url_suffix, **kwargs)


class QuestionCreate(LoginRequiredMixin, PermissionRequiredMixin, ObjectCreate):
    permission_required = 'is_staff'
    url_suffix = '/report/question/'
    template_name = "report/question/question_form.html"

    def get(self, request):
        return super(QuestionCreate, self).get(request, self.template_name, self.url_suffix)

    def post(self, request, **kwargs):
        expected_fields = ['reason_type', 'priority_type', 'description', 'is_resolved']
        redirect_url = 'report-question-index'
        return super(QuestionCreate, self).post(request=request, template_name=self.template_name,
                                                url_suffix=self.url_suffix,
                                                expected_fields=expected_fields,
                                                redirect_url=redirect_url,
                                                **kwargs)


class QuestionUpdate(LoginRequiredMixin, PermissionRequiredMixin, ObjectUpdate):
    permission_required = 'is_staff'
    url_suffix = '/report/question/'
    template_name = "report/question/question_form.html"

    def get(self, request, **kwargs):
        return super(QuestionUpdate, self).get(request, self.template_name, self.url_suffix, **kwargs)

    def post(self, request, **kwargs):
        expected_fields = ['reason_type', 'priority_type', 'description', 'is_resolved']
        redirect_url = 'report-question-index'
        return super(QuestionUpdate, self).post(request=request, template_name=self.template_name,
                                                url_suffix=self.url_suffix,
                                                expected_fields=expected_fields,
                                                redirect_url=redirect_url,
                                                **kwargs)


class QuestionDelete(LoginRequiredMixin, PermissionRequiredMixin, ObjectDelete):
    permission_required = 'is_staff'
    url_suffix = '/report/question/'
    redirect_url = 'report-question-index'

    def get(self, request, **kwargs):
        return super(QuestionDelete, self).get(request=request,
                                               url_suffix=self.url_suffix,
                                               redirect_url=self.redirect_url,
                                               **kwargs)


class SuspiciousIndex(LoginRequiredMixin, PermissionRequiredMixin, ObjectIndex):
    permission_required = 'is_staff'
    url_suffix = '/report/suspicious/'
    template_name = "report/suspicious/suspicious_index.html"

    def get(self, request):
        return super(SuspiciousIndex, self).get(request, self.template_name, self.url_suffix)


class SuspiciousDetail(LoginRequiredMixin, PermissionRequiredMixin, ObjectDetail):
    permission_required = 'is_staff'
    url_suffix = '/report/suspicious/'
    template_name = "report/suspicious/suspicious_detail.html"

    def get(self, request, **kwargs):
        return super(SuspiciousDetail, self).get(request, self.template_name, self.url_suffix, **kwargs)


class SuspiciousCreate(LoginRequiredMixin, PermissionRequiredMixin, ObjectCreate):
    permission_required = 'is_staff'
    url_suffix = '/report/suspicious/'
    template_name = "report/suspicious/suspicious_form.html"

    def get(self, request):
        return super(SuspiciousCreate, self).get(request, self.template_name, self.url_suffix)

    def post(self, request, **kwargs):
        expected_fields = ['reason_type', 'priority_type', 'description', 'is_resolved', 'url', 'incident_date']
        redirect_url = 'report-suspicious-index'
        return super(SuspiciousCreate, self).post(request=request, template_name=self.template_name,
                                                  url_suffix=self.url_suffix,
                                                  expected_fields=expected_fields,
                                                  redirect_url=redirect_url,
                                                  **kwargs)


class SuspiciousUpdate(LoginRequiredMixin, PermissionRequiredMixin, ObjectUpdate):
    permission_required = 'is_staff'
    url_suffix = '/report/suspicious/'
    template_name = "report/suspicious/suspicious_form.html"

    def get(self, request, **kwargs):
        return super(SuspiciousUpdate, self).get(request, self.template_name, self.url_suffix, **kwargs)

    def post(self, request, **kwargs):
        expected_fields = ['reason_type', 'priority_type', 'description', 'is_resolved', 'url', 'incident_date']
        redirect_url = 'report-suspicious-index'
        return super(SuspiciousUpdate, self).post(request=request, template_name=self.template_name,
                                                  url_suffix=self.url_suffix,
                                                  expected_fields=expected_fields,
                                                  redirect_url=redirect_url,
                                                  **kwargs)


class SuspiciousDelete(LoginRequiredMixin, PermissionRequiredMixin, ObjectDelete):
    permission_required = 'is_staff'
    url_suffix = '/report/suspicious/'
    redirect_url = 'report-suspicious-index'

    def get(self, request, **kwargs):
        return super(SuspiciousDelete, self).get(request=request,
                                                 url_suffix=self.url_suffix,
                                                 redirect_url=self.redirect_url,
                                                 **kwargs)

class ResponseCreate(LoginRequiredMixin, PermissionRequiredMixin, ObjectCreate):
    permission_required = 'is_staff'
    url_suffix = '/report/response/'
    template_name = "report/question/question_index.html"

    def get(self, request):
        return super(ResponseCreate, self).get(request, self.template_name, self.url_suffix)

    def post(self, request, **kwargs):
        expected_fields = ['reason_type', 'priority_type', 'description', 'is_resolved', 'url', 'incident_date']
        redirect_url = 'report-response-index'
        return super(ResponseCreate, self).post(request=request, template_name=self.template_name,
                                                url_suffix=self.url_suffix,
                                                expected_fields=expected_fields,
                                                redirect_url=redirect_url,
                                                **kwargs)


class ResponseUpdate(LoginRequiredMixin, PermissionRequiredMixin, ObjectUpdate):
    permission_required = 'is_staff'
    url_suffix = '/report/response/'
    template_name = "report/question/question_index.html"

    def get(self, request, **kwargs):
        return super(ResponseUpdate, self).get(request, self.template_name, self.url_suffix, **kwargs)

    def post(self, request, **kwargs):
        expected_fields = ['reason_type', 'priority_type', 'description', 'is_resolved', 'url', 'incident_date']
        redirect_url = 'report-response-index'
        return super(ResponseUpdate, self).post(request=request, template_name=self.template_name,
                                                url_suffix=self.url_suffix,
                                                expected_fields=expected_fields,
                                                redirect_url=redirect_url,
                                                **kwargs)


class ResponseDelete(LoginRequiredMixin, PermissionRequiredMixin, ObjectDelete):
    permission_required = 'is_staff'
    url_suffix = '/report/response/'
    redirect_url = 'report-response-index'

    def get(self, request, **kwargs):
        return super(ResponseDelete, self).get(request=request,
                                               url_suffix=self.url_suffix,
                                               redirect_url=self.redirect_url,
                                               **kwargs)
