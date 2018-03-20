from django.urls import path
from . import views
from django.conf.urls import url


urlpatterns = [
    path("", views.index, name="index"),
    url(r'^yt/$', views.yt, name="yt"),
    url(r'^search/$', views.search, name="search"),
    url(r'^data/$', views.data, name="data"),
    url(r'^yt/ytsearch/$', views.ytsearch, name="ytsearch"),
    url(r'^ytdata/$', views.ytdata, name="ytdata"),
]