from django.conf.urls import patterns, include, url

from berth.project import views

urlpatterns = patterns('',
    url(r'^project/new/?$', views.CreateProject.as_view(), name='new-project'),
)
