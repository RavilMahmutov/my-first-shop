from django.conf.urls import url
from . import views


urlpatterns = [
	url(r'^$', views.post_list, name = 'post_list'),
	url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail, name = 'post_detail'),
	url(r'^catefory/(?P<pk>[0-9]+)/$', views.category, name = 'category'),
	url(r'^good/(?P<pk>[0-9]+)/$', views.good_detail, name = 'good_detail'),
]

