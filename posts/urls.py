from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^$', "posts.views.post_list"),
    url(r'^create/$', "posts.views.post_create"),
    url(r'^delete/$', "posts.views.post_delete"),
    url(r'^(?P<id>\d+)/$', "posts.views.post_detail", name='detail'),
    url(r'^update/$', "posts.views.post_update"),
]
