from django.conf.urls import patterns, include, url

from berth.webhooks import views

urlpatterns = patterns('',
    url(r'^github/?$', views.GithubWebhook.as_view(), name='gh-webhook'),
)
