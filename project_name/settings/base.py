# Django settings for dj_layout project.
from django.conf.global_settings import *

#==============================================================================
# Generic Django project settings
#============================================================================== 

DEBUG = True
TEMPLATE_DEBUG = DEBUG

SITE_ID = 1

TIME_ZONE = 'Europe/Copenhagen'

USE_TZ = True

USE_I18N = True

USE_L10N = True

LANGUAGE_CODE = 'en-gb'

LANGUAGES = (
    ('en', 'English'),
)

SECRET_KEY = '{{ secret_key }}'


INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    # Uncomment the next line to enable admin documentation:
    #'django.contrib.admindocs',
    #Project apps here.
    
    #'south',
)

#==============================================================================
# Calculation of directories relative to the project module location
#==============================================================================

import os
import sys
import {{ project_name }} as project_module

PROJECT_DIR = os.path.dirname(os.path.realpath(project_module.__file__))
BASE_PATH     = os.path.dirname(PROJECT_DIR)
sys.path.insert(0, os.path.join(BASE_PATH, "apps"))

media_dir = os.path.join(BASE_PATH, 'media')

if not os.path.exists(media_dir):
	os.mkdir(media_dir)

#==============================================================================
# Project URLS and media settings
#==============================================================================

ROOT_URLCONF = '{{ project_name }}.urls'

LOGIN_URL = '/login/'

LOGOUT_URL = '/logout/'

LOGIN_REDIRECT_URL = '/'

STATIC_URL = '/static/'

MEDIA_URL = '/uploads/'

STATIC_ROOT = os.path.join(media_dir, 'static')

MEDIA_ROOT = os.path.join(media_dir, 'uploads')

STATICFILES_DIRS = (
    os.path.join(PROJECT_DIR, 'static'),
)

#==============================================================================
# Templates
#==============================================================================

TEMPLATE_DIRS = (
    os.path.join(PROJECT_DIR, 'templates'),
)

TEMPLATE_CONTEXT_PROCESSORS += (
)

#==============================================================================
# Middleware
#==============================================================================

MIDDLEWARE_CLASSES += (
)

#==============================================================================
# Auth / security
#==============================================================================

AUTHENTICATION_BACKENDS += (
)

#==============================================================================
# Miscellaneous project settings
#==============================================================================

#==============================================================================
# Third party app settings
#==============================================================================
