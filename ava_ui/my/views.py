import logging

from django.contrib.auth.mixins import LoginRequiredMixin

from ava_ui.abstract.views import ObjectIndex, ObjectDetail

log = logging.getLogger(__name__)


class LearningHistoryIndex(LoginRequiredMixin,  ObjectIndex):
    url_suffix = '/my/learn/history/'
    template_name = "my/learning/history/learning_history_index.html"

    def get(self, request):
        return super(LearningHistoryIndex, self).get(request, self.template_name, self.url_suffix)

class TestResultsIndex(LoginRequiredMixin,  ObjectIndex):
    url_suffix = '/my/test/results'
    template_name = "my/test/results_index.html"

    def get(self, request):
        return super(TestResultsIndex, self).get(request, self.template_name, self.url_suffix)

class PeopleIndex(LoginRequiredMixin,  ObjectIndex):
    url_suffix = '/my/people'
    template_name = "organize/person/person_index.html"

    def get(self, request):
        return super(PeopleIndex, self).get(request, self.template_name, self.url_suffix)

class QuestionsIndex(LoginRequiredMixin,  ObjectIndex):
    url_suffix = '/my/questions'
    template_name = "report/question/question_index.html"

    def get(self, request):
        return super(QuestionsIndex, self).get(request, self.template_name, self.url_suffix)

class SuspiciousIndex(LoginRequiredMixin,  ObjectIndex):
    url_suffix = '/my/suspicious'
    template_name = "report/suspicious/suspicious_index.html"

    def get(self, request):
        return super(QuestionsIndex, self).get(request, self.template_name, self.url_suffix)

class LearningQueueIndex(LoginRequiredMixin,  ObjectIndex):
    url_suffix = '/my/learn/queue/'
    template_name = "my/learning/queue/learning_queue_index.html"

    def get(self, request):
        return super(LearningQueueIndex, self).get(request, self.template_name, self.url_suffix)


class LearningProfileIndex(LoginRequiredMixin,  ObjectIndex):
    url_suffix = '/my/learn/profile/'
    template_name = "my/learning/profile/learning_profile.html"

    def get(self, request):
        return super(LearningProfileIndex, self).get(request, self.template_name, self.url_suffix)


class FriendsListIndex(LoginRequiredMixin,  ObjectIndex):
    url_suffix = '/my/friends/'
    template_name = "my/friends/friends_index.html"

    def get(self, request):
        return super(FriendsListIndex, self).get(request, self.template_name, self.url_suffix)


class ActivityLogIndex(LoginRequiredMixin,  ObjectIndex):
    url_suffix = '/my/activity/'
    template_name = "my/profile/history/profile_history_index.html"

    def get(self, request):
        return super(ActivityLogIndex, self).get(request, self.template_name, self.url_suffix)


class ScoreCardIndex(LoginRequiredMixin,  ObjectIndex):
    url_suffix = '/my/scorecard/'
    template_name = "my/scorecard/scorecard_index.html"

    def get(self, request):
        return super(ScoreCardIndex, self).get(request, self.template_name, self.url_suffix)


