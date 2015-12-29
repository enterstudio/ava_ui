import logging

from ava_ui.abstract.views import ObjectIndex, ObjectDetail

log = logging.getLogger(__name__)


class ProfileIndex(ObjectIndex):
    url_suffix = '/my/profile/'
    template_name = "my/profile/profile.html"

    def get(self, request):
        return super(ProfileIndex, self).get(request, self.template_name, self.url_suffix)


class LearningHistoryIndex(ObjectIndex):
    url_suffix = '/my/learn/history/'
    template_name = "my/learning/history/learning_history_index.html"

    def get(self, request):
        return super(LearningHistoryIndex, self).get(request, self.template_name, self.url_suffix)


class LearningQueueIndex(ObjectIndex):
    url_suffix = '/my/learn/queue/'
    template_name = "my/learning/queue/learning_queue_index.html"

    def get(self, request):
        return super(LearningQueueIndex, self).get(request, self.template_name, self.url_suffix)


class LearningProfileIndex(ObjectIndex):
    url_suffix = '/my/learn/profile/'
    template_name = "my/learning/profile/learning_profile.html"

    def get(self, request):
        return super(LearningProfileIndex, self).get(request, self.template_name, self.url_suffix)


class FriendsListIndex(ObjectIndex):
    url_suffix = '/my/friends/'
    template_name = "my/friends/friends_index.html"

    def get(self, request):
        return super(FriendsListIndex, self).get(request, self.template_name, self.url_suffix)


class ActivityLogIndex(ObjectIndex):
    url_suffix = '/my/activity/'
    template_name = "my/profile/history/profile_history_index.html"

    def get(self, request):
        return super(ActivityLogIndex, self).get(request, self.template_name, self.url_suffix)


class ScoreCardIndex(ObjectIndex):
    url_suffix = '/my/scorecard/'
    template_name = "my/scorecard/scorecard_index.html"

    def get(self, request):
        return super(ScoreCardIndex, self).get(request, self.template_name, self.url_suffix)


