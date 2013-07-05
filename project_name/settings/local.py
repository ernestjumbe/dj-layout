from {{ project_name }}.settings.base import *

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

INSTALLED_APPS += (
    'debug_toolbar',
  
)

#==============================================================================
# Miscellaneous local settings
#==============================================================================

#Debug toolbar settings
#----------------------

INTERNAL_IPS = ('127.0.0.1',)


DEBUG_TOOLBAR_PANELS = (
    'debug_toolbar.panels.version.VersionDebugPanel',
    'debug_toolbar.panels.timer.TimerDebugPanel',
    'debug_toolbar.panels.settings_vars.SettingsVarsDebugPanel',
    'debug_toolbar.panels.headers.HeaderDebugPanel',
    'debug_toolbar.panels.request_vars.RequestVarsDebugPanel',
    'debug_toolbar.panels.template.TemplateDebugPanel',
    'debug_toolbar.panels.sql.SQLDebugPanel',
    'debug_toolbar.panels.signals.SignalDebugPanel',
    'debug_toolbar.panels.logger.LoggingPanel',
)

DEBUG_TOOLBAR_CONFIG = {
    'INTERCEPT_REDIRECTS': False,
}

def show_toolbar(request):
    return True
SHOW_TOOLBAR_CALLBACK = show_toolbar