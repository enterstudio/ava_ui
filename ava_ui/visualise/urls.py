from django.conf.urls import url

from ava_ui.visualise import views

urlpatterns = [
    url(r'^graph/$', views.GraphIndex.as_view(), name='visualise-index'),
    url(r'^graph/(?P<pk>\d+)/data/$', views.graph_data, name='visualise-graph-view'),

]
