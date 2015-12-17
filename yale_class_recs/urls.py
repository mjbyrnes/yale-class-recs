from django.conf.urls import url, include

from . import views

urlpatterns = [
	url(r'^$', views.CoverView.as_view(), name='cover'),
	url(r'^login$', 'django.contrib.auth.views.login',
		{'template_name': 'registration/login.html', 'extra_context': {'next':'accounts/profile'}}),
	url(r'^logout$', 'django.contrib.auth.views.logout',
		{'template_name': 'registration/logout.html', 'extra_context': {}}),
	url(r'^new_user_info$', views.get_new_user_info, name='new_user_info'),
	url(r'^accounts/profile$', views.user_home, name='user_home_page'),
	url(r'^accounts/edit_info$', views.edit_info, name="edit_info"),
	url(r'^info$', views.get_name, name='info'),
]