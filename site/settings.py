import os
import sys

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    # ('Your Name', 'your_email@domain.com'),
)

MANAGERS = ADMINS

DATABASE_ENGINE = 'sqlite3'
DATABASE_NAME = os.path.join(os.path.dirname(__file__), 'site.db')
DATABASE_USER = ''             # Not used with sqlite3.
DATABASE_PASSWORD = ''         # Not used with sqlite3.
DATABASE_HOST = ''             # Set to empty string for localhost. Not used with sqlite3.
DATABASE_PORT = ''             # Set to empty string for default. Not used with sqlite3.

TIME_ZONE = 'America/'

LANGUAGE_CODE = 'en-us'

USE_I18N = True

MEDIA_ROOT = os.path.join(os.path.dirname(__file__), 'media/')
MEDIA_URL = '/media/'
ADMIN_MEDIA_PREFIX = '/admin_media/'

SECRET_KEY = 't8ft52-2@20f2q9p^7*#s$!pnj-b(_pq%%&kbp1##!z6h#j)2^'

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.core.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.request',
    # Custom context processors go here

)

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.load_template_source',
    'django.template.loaders.app_directories.load_template_source',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
)

TEMPLATE_DIRS = (
    os.path.join(os.path.dirname(__file__), "templates"),
)

# For Windows. Edit if needed
if sys.platform == 'win32':
    TEMPLATE_DIRS = (
        os.path.join(os.path.dirname(__file__), "templates"),
    ) 

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.admin',

)

ROOT_URLCONF = 'urls'
SITE_ID = 1

LANGUAGES = (
    ('en', 'English'),
    )

