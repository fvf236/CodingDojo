from django.conf.urls import url
from . import views
from django import forms


urlpatterns = [
  url(r'^$', views.index),
  url(r'^new', views.new),
  url(r'^create', views.create),
  url(r'^(?P<num>[0-9]+)/$', views.show),
  url(r'^(?P<num>[0-9]+)/edit', views.edit),
  url(r'^(?P<num>[0-9]+)/delete', views.destroy),
]
