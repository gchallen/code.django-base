import os
import sys
 
path = '/home/challen/code/django'
if path not in sys.path:
    sys.path.append(path)
path = '/home/challen/code/django/production'
if path not in sys.path:
    sys.path.append(path)
 
os.environ['DJANGO_SETTINGS_MODULE'] = 'production.settings'
 
import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
