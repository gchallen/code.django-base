import os
ROOT_PATH = os.path.dirname(__file__)
DEBUG = True
TEMPLATE_DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(ROOT_PATH, '/db/sqlite.db'),
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}
MEDIA_ROOT = os.path.join(ROOT_PATH, 'media')
MEDIA_URL = 'http://127.0.0.1:8000/media/'
ADMIN_MEDIA_PREFIX = '/static/admin/'
STATIC_ROOT = os.path.join(ROOT_PATH, 'static')
STATIC_URL = '/static/'
