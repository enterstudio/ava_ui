import logging

from ava_ui.abstract.views import ObjectIndex, ObjectDetail, ObjectCreate

log = logging.getLogger(__name__)


class ModuleIndex(ObjectIndex):
    url_suffix = '/learn/module/'
    template_name = "learn/module/module_index.html"

    def get(self, request):
        return super(ModuleIndex, self).get(request, self.template_name, self.url_suffix)


class ModuleDetail(ObjectDetail):
    url_suffix = '/learn/module/'
    template_name = "learn/module/module_detail.html"

    def get(self, request, **kwargs):
        return super(ModuleDetail, self).get(request, self.template_name, self.url_suffix, **kwargs)


class ModuleCreate(ObjectCreate):
    url_suffix = '/learn/module/'
    template_name = "learn/module/module_form.html"

    def get(self, request):
        return super(ModuleIndex, self).get(request, self.template_name, self.url_suffix)

    def post(self, request, **kwargs):
        expected_fields = ['name', 'description', 'module_url']
        redirect_url = 'learn-module-list'
        return super(ModuleCreate, self).post(request=request, template_name=self.template_name,
                                              url_suffix=self.url_suffix,
                                              expected_fields=expected_fields,
                                              redirect_url=redirect_url,
                                              **kwargs)

class RoleIndex(ObjectIndex):
    url_suffix = '/learn/role/'
    template_name = "learn/role/role_index.html"

    def get(self, request):
        return super(RoleIndex, self).get(request, self.template_name, self.url_suffix)


class RoleDetail(ObjectDetail):
    url_suffix = '/learn/role/'
    template_name = "learn/role/role_detail.html"

    def get(self, request, **kwargs):
        return super(RoleDetail, self).get(request, self.template_name, self.url_suffix, **kwargs)


class RoleCreate(ObjectCreate):
    url_suffix = '/learn/role/'
    template_name = "learn/role/role_form.html"

    def get(self, request):
        return super(RoleIndex, self).get(request, self.template_name, self.url_suffix)

    def post(self, request, **kwargs):
        expected_fields = ['name', 'description']
        redirect_url = 'learn-role-list'
        return super(RoleCreate, self).post(request=request, template_name=self.template_name,
                                              url_suffix=self.url_suffix,
                                              expected_fields=expected_fields,
                                              redirect_url=redirect_url,
                                              **kwargs)
class PathIndex(ObjectIndex):
    url_suffix = '/learn/path/'
    template_name = "learn/path/path_index.html"

    def get(self, request):
        return super(PathIndex, self).get(request, self.template_name, self.url_suffix)


class PathDetail(ObjectDetail):
    url_suffix = '/learn/path/'
    template_name = "learn/path/path_detail.html"

    def get(self, request, **kwargs):
        return super(PathDetail, self).get(request, self.template_name, self.url_suffix, **kwargs)


# TODO THIS PROBABLY DOESN'T WORK DUE TO RELATIONSHIPS ..... GAHHHHHHH
class PathCreate(ObjectCreate):
    url_suffix = '/learn/path/'
    template_name = "learn/path/path_form.html"

    def get(self, request):
        return super(PathIndex, self).get(request, self.template_name, self.url_suffix)

    def post(self, request, **kwargs):
        expected_fields = ['name', 'description', 'module', 'parent_module', 'role']
        redirect_url = 'learn-path-list'
        return super(PathCreate, self).post(request=request, template_name=self.template_name,
                                              url_suffix=self.url_suffix,
                                              expected_fields=expected_fields,
                                              redirect_url=redirect_url,
                                              **kwargs)


