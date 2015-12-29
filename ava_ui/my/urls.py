from django.conf.urls import url

from .views import *


urlpatterns = [
    url(r'^profile/$', ProfileIndex.as_view(template_name=""),
        name="my-profile-index"),

    url(r'^profile/(?P<pk>[0-9]+)/$', ProfileDetail.as_view(template_name=""),
        name="my-profile-detail"),

    url(r'^profile/history/$', ActivityLogIndex.as_view(template_name=""),
        name="my-profile-history-index"),

    url(r'^profile/history/(?P<pk>[0-9]+)/$', ActivityLogDetail.as_view(template_name=""),
        name="my-profile-history-detail"),

    url(r'^friends/$', FriendsListIndex.as_view(template_name=""),
        name="my-friends-index"),

    url(r'^friends/(?P<pk>[0-9]+)/$', FriendsListDetail.as_view(template_name=""),
        name="my-friends-detail"),
    
    url(r'^scorecard/$', ScoreCardIndex.as_view(template_name=""),
        name="my-scorecard-index"),

    url(r'^scorecard/(?P<pk>[0-9]+)/$', ScoreCardDetail.as_view(template_name=""),
        name="my-scorecard-detail"),

    url(r'^learning/history/$', LearningHistoryIndex.as_view(template_name=""),
        name="my-learning-history-index"),

    url(r'^learning/history/(?P<pk>[0-9]+)/$', LearningHistoryDetail.as_view(template_name=""),
        name="my-learning-history-detail"),

    url(r'^learning/queue/$', LearningQueueIndex.as_view(template_name=""),
        name="my-learning-queue-index"),

    url(r'^learning/queue/(?P<pk>[0-9]+)/$', LearningQueueDetail.as_view(template_name=""),
        name="my-learning-queue-detail"),

    url(r'^learning/profile/$', LearningProfileIndex.as_view(template_name=""),
        name="my-learning-profile-index"),

    url(r'^learning/profile/(?P<pk>[0-9]+)/$', LearningProfileDetail.as_view(template_name=""),
        name="my-learning-profile-detail"),


    
]
