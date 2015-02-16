from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ayee.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^', include('input.urls', namespace="input")),
    url(r'^admin/', include(admin.site.urls)),
)
