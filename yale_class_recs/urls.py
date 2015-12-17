from django.conf.urls import url, include
from django.contrib.auth.views import login, logout, password_change, password_change_done
from . import views

urlpatterns = [
	url(r'^$', views.CoverView.as_view(), name='cover'),
	url(r'^about/$', views.about, name="about"),
	url(r'^login/$', login,
		{'template_name': 'registration/login.html', 'extra_context': 
		{'next':'/yale_class_recs/accounts/profile'}}, name='login'),
	url(r'^logout/$', logout,
		{'template_name': 'registration/logout.html', 'extra_context': {}}, name='logout'),
	url(r'^password_change/$', password_change,
		{'template_name': 'registration/password_change.html',
		'post_change_redirect': 'yale_class_recs:password_change_done', 'extra_context': {}},
		name='password_change'),
	url(r'^password_change/done/$', password_change_done,
		{'template_name': 'registration/password_change_done.html', 'extra_context': {}},
		name='password_change_done'),
	url(r'^new_user_info/$', views.get_new_user_info, name='new_user_info'),
	url(r'^accounts/profile/$', views.user_home, name='user_home_page'),
	url(r'^accounts/edit_info/$', views.edit_info, name="edit_info"),
	url(r'^search/$', views.search, name='search'),
]