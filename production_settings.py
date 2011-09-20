import os
from settings import INSTALLED_APPS

ROOT_PATH = os.path.dirname(__file__)
DEBUG = True
TEMPLATE_DEBUG = True

DATABASES = {
      'default': {
                'ENGINE': 'django.db.backends.mysql',
                'OPTIONS': {
                              'read_default_file': os.path.join(ROOT_PATH, 'db/my.cnf'),
                          },
            }
}
MEDIA_ROOT = os.path.join(ROOT_PATH, 'media')
MEDIA_URL = 'http://blue.cse.buffalo.edu/media/'
ADMIN_MEDIA_PREFIX = '/static/admin/'
STATIC_ROOT = os.path.join(ROOT_PATH, 'static')
STATIC_URL = '/static/'
AWS_ACCESS_KEY_ID = 'AKIAJGTF2EAMZBLFWPIA'
AWS_SECRET_ACCESS_KEY = '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'

TEMPLATE_DIRS = (
  os.path.join(ROOT_PATH, 'course/templates'),
)

INSTALLED_APPS += ('django_ses',)

EMAIL_BACKEND = 'django_ses.SESBackend'
#EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
