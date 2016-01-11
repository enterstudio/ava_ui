from django.conf.urls import url

from .views import *


urlpatterns = [

    url(r'^profile/history/$', ActivityLogIndex.as_view(),
        name="my-profile-history-index"),

    url(r'^friends/$', FriendsListIndex.as_view(),
        name="my-friends-index"),

    url(r'^people/$', PeopleIndex.as_view(),
        name="my-people-index"),

    url(r'^scorecard/$', ScoreCardIndex.as_view(),
        name="my-scorecard-index"),

    url(r'^learning/history/$', LearningHistoryIndex.as_view(),
        name="my-learning-history-index"),

    url(r'^learning/queue/$', LearningQueueIndex.as_view(),
        name="my-learning-queue-index"),

    url(r'^learning/profile/$', LearningProfileIndex.as_view(),
        name="my-learning-profile"),

    url(r'^results/$', TestResultsIndex.as_view(),
        name="my-results-index"),

    url(r'^questions/$', QuestionsIndex.as_view(),
        name="my-questions-index"),

    url(r'^reports/$', SuspiciousIndex.as_view(),
        name="my-reports-index"),
    
]
