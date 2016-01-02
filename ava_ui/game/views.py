import logging

from ava_ui.abstract.views import ObjectIndex, ObjectDetail, ObjectCreate, ObjectDelete

log = logging.getLogger(__name__)


class AchievementIndex(ObjectIndex):
    url_suffix = '/game/achievement/'
    template_name = "game/achievement/achievement_index.html"

    def get(self, request):
        return super(AchievementIndex, self).get(request, self.template_name, self.url_suffix)


class AchievementDetail(ObjectDetail):
    url_suffix = '/game/achievement/'
    template_name = "game/achievement/achievement_detail.html"

    def get(self, request, **kwargs):
        return super(AchievementDetail, self).get(request, self.template_name, self.url_suffix, **kwargs)


class AchievementCreate(ObjectCreate):
    url_suffix = '/game/achievement/'
    template_name = "game/achievement/achievement_form.html"

    def get(self, request):
        return super(AchievementCreate, self).get(request, self.template_name, self.url_suffix)

    def post(self, request, **kwargs):
        expected_fields = ['name', 'description', 'icon_url', 'score']
        redirect_url = 'game-achievement-index'
        return super(AchievementCreate, self).post(request=request, template_name=self.template_name,
                                                   url_suffix=self.url_suffix,
                                                   expected_fields=expected_fields,
                                                   redirect_url=redirect_url,
                                                   **kwargs)


# class AchievementDelete(ObjectDelete):
#     url_suffix = '/game/achievement/'
#     template_name = "confirm_delete.html"
#
#     def get(self, request):
#         return super(AchievementDelete, self).get(request, self.template_name, self.url_suffix)
#
#     def post(self, request, **kwargs):
#         redirect_url = 'game-achievement-index'
#         return super(AchievementDelete, self).post(request=request,
#                                                    url_suffix=self.url_suffix,
#                                                    redirect_url=redirect_url,
#                                                    **kwargs)
