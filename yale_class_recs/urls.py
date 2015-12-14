from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^$', views.CoverView.as_view(), name='cover'),
  url(r'info', views.get_name, name='info'),
]