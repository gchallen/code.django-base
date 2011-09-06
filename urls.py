from django.conf.urls.defaults import patterns, include, url
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import admin
admin.autodiscover()

# 23 Aug 2011 : GWA : Standard stuff. Admin interface and media.

urlpatterns = patterns('', 
                       url(r'^admin/', include(admin.site.urls)),
                       (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}))

# 23 Aug 2011 : GWA : Added for django-course.

urlpatterns += patterns('', (r'^course/', include('course.urls')))
