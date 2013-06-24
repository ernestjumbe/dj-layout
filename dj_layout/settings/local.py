from layout.settings.base import *

DEBUG = True
TEMPLATE_DEBUG = DEBUG

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

import os
import sys
import {{ project_name }} as project_module

PROJECT_DIR = os.path.dirname(os.path.realpath(project_module.__file__))
BASE_PATH     = os.path.dirname(PROJECT_DIR)

PYTHON_BIN = os.path.dirname(sys.executable)
ve_path = os.path.dirname(os.path.dirname(os.path.dirname(PROJECT_DIR)))
# Assume that the presence of 'activate_this.py' in the python bin/
# directory means that we're running in a virtual environment.
if os.path.exists(os.path.join(PYTHON_BIN, 'activate_this.py')):
    # We're running with a virtualenv python executable.
    VAR_ROOT = os.path.join(os.path.dirname(PYTHON_BIN), 'var')
elif ve_path and os.path.exists(os.path.join(ve_path, 'bin',
        'activate_this.py')):
    # We're running in [virtualenv_root]/src/[project_name].
    VAR_ROOT = os.path.join(ve_path, 'var')
else:
    # Set the variable root to a path in the project which is
    # ignored by the repository.
    VAR_ROOT = os.path.join(PROJECT_DIR, 'var')

if not os.path.exists(VAR_ROOT):
    os.mkdir(VAR_ROOT)

#==============================================================================
# Project URLS and media settings
#==============================================================================

STATIC_ROOT = os.path.join(VAR_ROOT, 'static')
MEDIA_ROOT = os.path.join(VAR_ROOT, 'uploads')

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