from django.conf.urls import url, include
from django.contrib.auth.views import login, logout, password_change, password_change_done
from . import views

urlpatterns = [
	# Cover Page
	url(r'^$', views.cover, name='cover'),
	# About
	url(r'^about/$', views.about, name="about"),
	# Login 
	url(r'^login/$', login,
		{'template_name': 'registration/login.html', 'extra_context': 
		{'next':'/yale_class_recs/accounts/profile'}}, name='login'),
	# Logout
	url(r'^logout/$', logout,
		{'template_name': 'registration/logout.html', 'extra_context': {}}, name='logout'),
	# Password change page
	url(r'^password_change/$', password_change,
		{'template_name': 'registration/password_change.html',
		'post_change_redirect': 'yale_class_recs:password_change_done', 'extra_context': {}},
		name='password_change'),
	url(r'^password_change/done/$', password_change_done,
		{'template_name': 'registration/password_change_done.html', 'extra_context': {}},
		name='password_change_done'),
	# Get New User Info
	url(r'^new_user_info/$', views.get_new_user_info, name='new_user_info'),
	# User Home/Profile
	url(r'^accounts/profile/$', views.user_home, name='user_home_page'),
	# Edit Personal Info
	url(r'^accounts/edit_info/$', views.edit_info, name="edit_info"),
	# Search
	url(r'^search/$', views.search, name='search'),
	# Course Information
	url(r'^search/(?P<course_id>[0-9]+)/$', views.course_info, name='course_info'),
	# Worksheet
	url(r'^worksheet/$', views.worksheet, name='worksheet')
]