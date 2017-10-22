from django.conf.urls import url
from . import views           # This line is new!
  
urlpatterns = [
    url(r'^$', views.index),
    url(r'^blogs_app$', views.index),
    url(r'^blogs_app/new', views.new),
    url(r'^blogs_app/create', views.create),
    url(r'^blogs_app/(?P<year>[0-9]+)$', views.show),
    url(r'^blogs_app/(?P<year>[0-9]+)/edit', views.edit),
    url(r'^blogs_app/(?P<year>[0-9]+)/delete', views.destroy)    # This line has changed!
]