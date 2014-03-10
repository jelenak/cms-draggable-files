from django.conf.urls import patterns, include, url
from django.conf.urls.i18n import i18n_patterns

from .views import file_upload
urlpatterns = patterns('',
    url('^', file_upload, name='file_upload'),
)
