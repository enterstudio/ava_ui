import logging

from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

from ava_ui.abstract.views import ObjectIndex, ObjectDetail, ObjectCreate, ObjectDelete, ObjectUpdate, \
    ObjectCreateRelated, ObjectUpdateRelated

log = logging.getLogger(__name__)


class ModuleIndex(LoginRequiredMixin, PermissionRequiredMixin, ObjectIndex):
    permission_required = 'is_staff'
    url_suffix = '/learn/module/'
    template_name = "learn/module/module_index.html"

    def get(self, request):
        return super(ModuleIndex, self).get(request, self.template_name, self.url_suffix)


class ModuleDetail(LoginRequiredMixin, PermissionRequiredMixin, ObjectDetail):
    permission_required = 'is_staff'
    url_suffix = '/learn/module/'
    template_name = "learn/module/module_detail.html"

    def get(self, request, **kwargs):
        return super(ModuleDetail, self).get(request, self.template_name, self.url_suffix, **kwargs)


class ModuleCreate(LoginRequiredMixin, PermissionRequiredMixin, ObjectCreateRelated):
    permission_required = 'is_staff'
    url_suffix = '/learn/module/'
    form_data_url = '/learn/form/'
    template_name = "learn/module/module_form.html"

    def get(self, request):
        return super(ModuleCreate, self).get(request=request, template_name=self.template_name,
                                             url_suffix=self.form_data_url)

    def post(self, request, **kwargs):
        expected_fields = ['name', 'description', 'module_url', 'parent']
        related_fields = ['parent']
        multiple_fields = ['path']
        redirect_url = 'learn-module-index'
        return super(ModuleCreate, self).post(request=request, template_name=self.template_name,
                                              url_suffix=self.url_suffix,
                                              expected_fields=expected_fields,
                                              related_fields=related_fields,
                                              multiple_fields=multiple_fields,
                                              redirect_url=redirect_url,
                                              **kwargs)


class ModuleUpdate(LoginRequiredMixin, PermissionRequiredMixin, ObjectUpdateRelated):
    permission_required = 'is_staff'
    url_suffix = '/learn/module/'
    form_data_url = '/learn/form/'
    template_name = "learn/module/module_form.html"

    def get(self, request, **kwargs):
        return super(ModuleUpdate, self).get(request=request, template_name=self.template_name,
                                             form_data_url_suffix=self.form_data_url, url_suffix=self.url_suffix,
                                             **kwargs)

    def post(self, request, **kwargs):
        expected_fields = ['name', 'description', 'module_url', 'parent']
        related_fields = ['parent']
        multiple_fields = ['path']
        redirect_url = 'learn-module-index'
        return super(ModuleUpdate, self).post(request=request, template_name=self.template_name,
                                              url_suffix=self.url_suffix,
                                              expected_fields=expected_fields,
                                              related_fields=related_fields,
                                              multiple_fields=multiple_fields,
                                              redirect_url=redirect_url,
                                              **kwargs)


class ModuleDelete(LoginRequiredMixin, PermissionRequiredMixin, ObjectDelete):
    permission_required = 'is_staff'
    url_suffix = '/learn/module/'
    redirect_url = 'learn-module-index'

    def get(self, request, **kwargs):
        return super(ModuleDelete, self).get(request=request,
                                             url_suffix=self.url_suffix,
                                             redirect_url=self.redirect_url,
                                             **kwargs)


class RoleIndex(LoginRequiredMixin, PermissionRequiredMixin, ObjectIndex):
    permission_required = 'is_staff'
    url_suffix = '/learn/role/'
    template_name = "learn/role/role_index.html"

    def get(self, request):
        return super(RoleIndex, self).get(request, self.template_name, self.url_suffix)


class RoleDetail(LoginRequiredMixin, PermissionRequiredMixin, ObjectDetail):
    permission_required = 'is_staff'
    url_suffix = '/learn/role/'
    template_name = "learn/role/role_detail.html"

    def get(self, request, **kwargs):
        return super(RoleDetail, self).get(request, self.template_name, self.url_suffix, **kwargs)

class RoleCreate(LoginRequiredMixin, PermissionRequiredMixin, ObjectCreateRelated):
    permission_required = 'is_staff'
    url_suffix = '/learn/role/'
    form_data_url = '/learn/form/'
    template_name = "learn/role/role_form.html"

    def get(self, request):
        return super(RoleCreate, self).get(request=request, template_name=self.template_name,
                                           url_suffix=self.form_data_url)

    def post(self, request, **kwargs):
        expected_fields = ['name', 'description']
        related_fields = []
        multiple_fields = ['path']
        redirect_url = 'learn-role-index'
        return super(RoleCreate, self).post(request=request, template_name=self.template_name,
                                            url_suffix=self.url_suffix,
                                            expected_fields=expected_fields,
                                            redirect_url=redirect_url,
                                            multiple_fields=multiple_fields,
                                            related_fields=related_fields,
                                            **kwargs)


class RoleUpdate(LoginRequiredMixin, PermissionRequiredMixin, ObjectUpdateRelated):
    permission_required = 'is_staff'
    url_suffix = '/learn/role/'
    form_data_url = '/learn/form/'
    template_name = "learn/role/role_form.html"

    def get(self, request, **kwargs):
        return super(RoleUpdate, self).get(request=request, template_name=self.template_name,
                                           url_suffix=self.url_suffix,
                                           form_data_url_suffix=self.form_data_url, **kwargs)

    def post(self, request, **kwargs):
        expected_fields = ['name', 'description']
        related_fields = []
        multiple_fields = ['path']
        redirect_url = 'learn-role-index'
        return super(RoleUpdate, self).post(request=request, template_name=self.template_name,
                                            url_suffix=self.url_suffix,
                                            expected_fields=expected_fields,
                                            redirect_url=redirect_url,
                                            multiple_fields=multiple_fields,
                                            related_fields=related_fields,
                                            **kwargs)


class RoleDelete(LoginRequiredMixin, PermissionRequiredMixin, ObjectDelete):
    permission_required = 'is_staff'
    url_suffix = '/learn/role/'
    redirect_url = 'learn-role-index'

    def get(self, request, **kwargs):
        return super(RoleDelete, self).get(request=request,
                                           url_suffix=self.url_suffix,
                                           redirect_url=self.redirect_url,
                                           **kwargs)


class PathIndex(LoginRequiredMixin, PermissionRequiredMixin, ObjectIndex):
    permission_required = 'is_staff'
    url_suffix = '/learn/path/'
    template_name = "learn/path/path_index.html"

    def get(self, request):
        return super(PathIndex, self).get(request, self.template_name, self.url_suffix)


class PathDetail(LoginRequiredMixin, PermissionRequiredMixin, ObjectDetail):
    permission_required = 'is_staff'
    url_suffix = '/learn/path/'
    template_name = "learn/path/path_detail.html"

    def get(self, request, **kwargs):
        return super(PathDetail, self).get(request, self.template_name, self.url_suffix, **kwargs)


class PathDelete(LoginRequiredMixin, PermissionRequiredMixin, ObjectDelete):
    permission_required = 'is_staff'
    url_suffix = '/learn/path/'
    redirect_url = 'learn-path-index'

    def get(self, request, **kwargs):
        return super(PathDelete, self).get(request=request,
                                           url_suffix=self.url_suffix,
                                           redirect_url=self.redirect_url,
                                           **kwargs)


class PathCreate(LoginRequiredMixin, PermissionRequiredMixin, ObjectCreateRelated):
    permission_required = 'is_staff'
    url_suffix = '/learn/path/'
    form_data_url = '/learn/form/'
    template_name = "learn/path/path_form.html"

    def get(self, request):
        return super(PathCreate, self).get(request=request, template_name=self.template_name,
                                           url_suffix=self.form_data_url)

    def post(self, request, **kwargs):
        expected_fields = ['name', 'description']
        related_fields = []
        multiple_fields = ['path_modules','path_roles']
        redirect_url = 'learn-path-index'
        return super(PathCreate, self).post(request=request, template_name=self.template_name,
                                            url_suffix=self.url_suffix,
                                            expected_fields=expected_fields,
                                            redirect_url=redirect_url,
                                            multiple_fields=multiple_fields,
                                            related_fields=related_fields,
                                            **kwargs)


class PathUpdate(LoginRequiredMixin, PermissionRequiredMixin, ObjectUpdateRelated):
    permission_required = 'is_staff'
    url_suffix = '/learn/path/'
    form_data_url = '/learn/form/'
    template_name = "learn/path/path_form.html"

    def get(self, request, **kwargs):
        return super(PathUpdate, self).get(request=request, template_name=self.template_name,
                                           url_suffix=self.url_suffix,
                                           form_data_url_suffix=self.form_data_url, **kwargs)

    def post(self, request, **kwargs):
        expected_fields = ['name', 'description']
        related_fields = []
        multiple_fields = ['path_modules','path_roles']
        redirect_url = 'learn-path-index'
        return super(PathUpdate, self).post(request=request, template_name=self.template_name,
                                            url_suffix=self.url_suffix,
                                            expected_fields=expected_fields,
                                            redirect_url=redirect_url,
                                            multiple_fields=multiple_fields,
                                            related_fields=related_fields,
                                            **kwargs)
