from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'berth.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    url(r'^', include('berth.site.urls')),
    url(r'^', include('berth.user.urls')),
    url(r'^', include('berth.project.urls')),
    url(r'^webhooks/', include('berth.webhooks.urls')),
)
