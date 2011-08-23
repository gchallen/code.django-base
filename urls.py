from django.conf.urls.defaults import patterns, include, url
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from django.contrib import admin
admin.autodiscover()

urlpatterns = []

urlpatterns += patterns('',
             url(r'^admin/', include(admin.site.urls)),
             (r'^course/', include('course.urls')))

urlpatterns += patterns('',
    (r'^media/(?P<path>.*)$',
     'django.views.static.serve',
     {'document_root': settings.MEDIA_ROOT}))
