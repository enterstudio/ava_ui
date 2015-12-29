import logging

from ava_ui.abstract.views import ObjectIndex, ObjectDetail

log = logging.getLogger(__name__)


class ProfileIndex(ObjectIndex):
    url_suffix = '/my/profile/'
    template_name = "my/profile/profile_index.html"

    def get(self, request):
        return super(ProfileIndex, self).get(request, self.template_name, self.url_suffix)


class LearningHistoryIndex(ObjectIndex):
    url_suffix = '/my/learning/history/'
    template_name = "my/learning/history_index.html"

    def get(self, request):
        return super(LearningHistoryIndex, self).get(request, self.template_name, self.url_suffix)


class LearningQueueIndex(ObjectIndex):
    url_suffix = '/my/learning/queue/'
    template_name = "my/learning/queue_index.html"

    def get(self, request):
        return super(LearningQueueIndex, self).get(request, self.template_name, self.url_suffix)


class LearningProfileIndex(ObjectIndex):
    url_suffix = '/my/learning/profile/'
    template_name = "my/learning/profile_index.html"

    def get(self, request):
        return super(LearningProfileIndex, self).get(request, self.template_name, self.url_suffix)


class FriendsListIndex(ObjectIndex):
    url_suffix = '/my/friends/'
    template_name = "my/friends/friends_index.html"

    def get(self, request):
        return super(FriendsListIndex, self).get(request, self.template_name, self.url_suffix)


class ActivityLogIndex(ObjectIndex):
    url_suffix = '/my/profile/history/'
    template_name = "my/profile/history_index.html"

    def get(self, request):
        return super(ActivityLogIndex, self).get(request, self.template_name, self.url_suffix)


class ScoreCardIndex(ObjectIndex):
    url_suffix = '/my/scorecard/'
    template_name = "my/scorecard/achievements_index.html"

    def get(self, request):
        return super(ScoreCardIndex, self).get(request, self.template_name, self.url_suffix)


class ProfileDetail(ObjectDetail):
    url_suffix = '/my/profile/'
    template_name = "my/profile/profile_detail.html"

    def get(self, request, **kwargs):
        return super(ProfileDetail, self).get(request, self.template_name, self.url_suffix, **kwargs)


class LearningHistoryDetail(ObjectDetail):
    url_suffix = '/my/learning/history/'
    template_name = "my/learning/history_detail.html"

    def get(self, request, **kwargs):
        return super(LearningHistoryDetail, self).get(request, self.template_name, self.url_suffix, **kwargs)


class LearningQueueDetail(ObjectDetail):
    url_suffix = '/my/learning/queue/'
    template_name = "my/learning/queue_detail.html"

    def get(self, request, **kwargs):
        return super(LearningQueueDetail, self).get(request, self.template_name, self.url_suffix, **kwargs)


class LearningProfileDetail(ObjectDetail):
    url_suffix = '/my/learning/profile/'
    template_name = "my/learning/profile_detail.html"

    def get(self, request, **kwargs):
        return super(LearningProfileDetail, self).get(request, self.template_name, self.url_suffix, **kwargs)


class FriendsListDetail(ObjectDetail):
    url_suffix = '/my/friends/'
    template_name = "my/friends/friends_detail.html"

    def get(self, request, **kwargs):
        return super(FriendsListDetail, self).get(request, self.template_name, self.url_suffix, **kwargs)


class ActivityLogDetail(ObjectDetail):
    url_suffix = '/my/profile/history/'
    template_name = "my/profile/history_detail.html"

    def get(self, request, **kwargs):
        return super(ActivityLogDetail, self).get(request, self.template_name, self.url_suffix, **kwargs)


class ScoreCardDetail(ObjectDetail):
    url_suffix = '/my/scorecard/'
    template_name = "my/scorecard/achievements_detail.html"

    def get(self, request, **kwargs):
        return super(ScoreCardDetail, self).get(request, self.template_name, self.url_suffix, **kwargs)
