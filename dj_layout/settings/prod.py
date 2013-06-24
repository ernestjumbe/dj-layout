"""Settings for Production Server"""
from {{ project_name }}.settings.base import *

DEBUG = False

ALOOWED_HOSTS = [
#    'example.com',
]

VAR_ROOT = '/var/www/{{ project_name }}'
MEDIA_ROOT = os.path.join(VAR_ROOT, 'uploads')
STATIC_ROOT = os.path.join(VAR_ROOT, 'static')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': '{{ project_name }}',
#        'USER': 'dbuser',
#        'PASSWORD': 'dbpassword',
    }
}

# WSGI_APPLICATION = '{{ project_name }}.wsgi.dev.application'