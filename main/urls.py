from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.main, name='main'),
    url(r'^post/$', views.post_list, name='post_list'),
    url(r'^post/detail/(?P<pk>[0-9]+)/$', views.post_detail, name='post_detail'),
   	url(r'^post/new/$', views.post_new, name='post_new'),
    url(r'^post/edit/(?P<pk>[0-9]+)/$', views.post_edit, name='post_edit'),
    url(r'^test/$', views.test_list, name='test_list'),
    url(r'^test/detail/(?P<pk>[0-9]+)/$', views.test_detail, name='test_detail'),
    url(r'^test/edit/(?P<pk>[0-9]+)/$', views.test_edit, name='test_edit'),
    url(r'^test/new/$', views.test_new, name='test_new'),
    url(r'^data/$', views.data, name="data"),
    url(r'^login/$', views.log_in, name='login'),
    url(r'^logout/$', views.logout_view, name='logout'),
]