from django.conf.urls import url, include

from . import views

urlpatterns = [
	url(r'^$', views.CoverView.as_view(), name='cover'),
	url('^', include('django.contrib.auth.urls')),
	url(r'^new_user_info$', views.get_new_user_info, name='new_user_info'),
	url(r'^home$', views.user_home, name='user_home_page'),
	url(r'^info$', views.get_name, name='info'),
]