from layout.settings.base import *

DEBUG = True
TEMPLATE_DEBUG = DEBUG

import os
import sys
import {{ project_name }} as project_module

PROJECT_DIR = os.path.dirname(os.path.realpath(project_module.__file__))
BASE_PATH     = os.path.dirname(PROJECT_DIR)

database_dir = os.path.join(BASE_PATH, 'databases')

if not os.path.exists(database_dir):
	os.mkdir(database_dir)

ADMINS = (
    ('You', 'your@email'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(database_dir, 'dev.db'),
    }
}

#==============================================================================
# Calculation of directories relative to the project module location
#==============================================================================

media_dir = os.path.join(BASE_PATH, 'media')

if not os.path.exists(media_dir):
	os.mkdir(media_dir)

#==============================================================================
# Project URLS and media settings
#==============================================================================

STATIC_ROOT = os.path.join(media_dir, 'static')
MEDIA_ROOT = os.path.join(media_dir, 'uploads')

STATICFILES_DIRS = (
    os.path.join(PROJECT_DIR, 'static'),
)

#==============================================================================
# Templates
#==============================================================================

TEMPLATE_DIRS = (
    os.path.join(BASE_PATH, 'templates'),
)

TEMPLATE_CONTEXT_PROCESSORS += (
)

#==============================================================================
# Miscellaneous local settings
#==============================================================================