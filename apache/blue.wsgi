import os
import sys
 
path = '/home/challen/code'
if path not in sys.path:
    sys.path.append(path)
path = '/home/challen/code/django-course-production'
if path not in sys.path:
    sys.path.append(path)
 
os.environ['DJANGO_SETTINGS_MODULE'] = 'django-course-production.settings'
 
import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
