from django.conf.urls import url
from . import views
from django.urls import path
# from django.urls.conf import include, re_path


urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    # url(r'^post/(?P<pk>[0-9]+)$', views.post_detail, name='post_detail'), #OR >
    # url('post/(?P<pk>[0-9]+)', views.post_detail, name='post_detail'), #OR >
    path('post/<int:pk>', views.post_detail, name='post_detail'),
    url(r'^post/create/$', views.post_create, name='post_create'),
    url(r'^post/(?P<pk>[0-9]+)/edit/$', views.post_edit, name='post_edit'),
    url(r'^post/(?P<pk>[0-9]+)/delete/$',
        views.post_delete, name='post_delete'),
]
