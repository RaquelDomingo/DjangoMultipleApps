from django.conf.urls import url
from . import views           # This line is new!
  
urlpatterns = [
    url(r'^$', views.index),
    url(r'^surveys_app/new', views.new),
        # This line has changed!
]