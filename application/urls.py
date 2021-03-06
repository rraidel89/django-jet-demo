from django.conf.urls import patterns, include, url
from django.contrib import admin
from jet.dashboard.dashboard_modules import google_analytics_views

admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^jet/', include('jet.urls', 'jet')),
    url(r'^jet/dashboard/', include('jet.dashboard.urls', 'jet-dashboard')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^ckeditor/', include('ckeditor.urls')),
    url(r'^tinymce/', include('tinymce.urls')),
)
