from django.conf.urls import patterns, include, url

from berth.user import views

urlpatterns = patterns('',
    url(r'^api/0/user/?$', views.CreateUser.as_view(), name='create-user'),
    url(r'^api/0/user/auth/?$', views.SignIn.as_view(), name='sign-in'),
)
