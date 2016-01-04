from django.conf.urls import url

from .views import *

urlpatterns = [
    url(r'^achievement/$', AchievementIndex.as_view(),
        name="game-achievement-index"),

    url(r'^achievement/new/$', AchievementCreate.as_view(),
        name="game-achievement-create"),

    url(r'^achievement/(?P<pk>[0-9]+)/$', AchievementDetail.as_view(),
        name="game-achievement-detail"),

    url(r'^achievement/update/(?P<pk>[0-9]+)/$', AchievementUpdate.as_view(),
        name="game-achievement-update"),

    url(r'^achievement/delete/(?P<pk>[0-9]+)/$', AchievementDelete.as_view(),
        name="game-achievement-delete"),

]
