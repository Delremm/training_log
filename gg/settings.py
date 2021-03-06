# Django settings for gg project.
import os

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    # ('Your Name', 'your_email@example.com'),
)

MANAGERS = ADMINS

if os.environ.get('django_local', 0 ):

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
            'NAME': 'base.db',                      # Or path to database file if using sqlite3.
            # The following settings are not used with sqlite3:
            'USER': '',
            'PASSWORD': '',
            'HOST': '',                      # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
            'PORT': '',                      # Set to empty string for default.
        }
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
            'NAME': 'training_log',                      # Or path to database file if using sqlite3.
            # The following settings are not used with sqlite3:
            'USER': 'training_log',
            'PASSWORD': '314159',
            'HOST': '',                      # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
            'PORT': '',                      # Set to empty string for default.
        }
    }

EMAIL_HOST = 'smtp.webfaction.com'
EMAIL_HOST_USER = 'training_log'
EMAIL_HOST_PASSWORD = 'boloto'
DEFAULT_FROM_EMAIL = 'admin@training_log.com'
SERVER_EMAIL = 'admin@training_log.com'

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'America/Chicago'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'ru-RU'
LOCALE_PATHS = (
    os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'locale')),
)

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT = '/home/delremm/webapps/training_log_static/media/'

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = '/media/'

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
STATIC_ROOT = '/home/delremm/webapps/training_log_static/' #'D:/glushaev/work/gg/static/'


# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = '/static/'
# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"


# Additional locations of static files
STATICFILES_DIRS = (
    os.path.join(os.path.dirname(__file__), '..', 'static'),
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'e$l1=wvi$rz$^0)&amp;st$hr735@um^%ekqf%(u0&amp;6+r8$(tl2c-q'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'gg.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'gg.wsgi.application'


import django.conf.global_settings as DEFAULT_SETTINGS

MIDDLEWARE_CLASSES = DEFAULT_SETTINGS.MIDDLEWARE_CLASSES + (
    #'fiber.middleware.ObfuscateEmailAddressMiddleware',
    #'fiber.middleware.AdminPageMiddleware',
)
TEMPLATE_CONTEXT_PROCESSORS = DEFAULT_SETTINGS.TEMPLATE_CONTEXT_PROCESSORS + (
    'django.core.context_processors.request',
    'social_auth.context_processors.social_auth_by_name_backends',
    'social_auth.context_processors.social_auth_backends',
    'social_auth.context_processors.social_auth_by_type_backends',
    'social_auth.context_processors.social_auth_login_redirect',
    'django.core.context_processors.i18n',
)

TEMPLATE_DIRS = (os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'templates')),)#('D:/glushaev/work/gg/templates',)

STATICFILES_FINDERS = STATICFILES_FINDERS + (
    'compressor.finders.CompressorFinder',
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Uncomment the next line to enable the admin:
    'django.contrib.admin',
    'django.contrib.comments',
    'foo',
    'log_app',
    'mptt',
    'compressor',
    'fiber',
    #'easy_thumbnails',
    'rest_framework',
    'django_verbatim',
    'south',
    'registration',
    'registration_email',
    'social_auth',
)

ACCOUNT_ACTIVATION_DAYS = 7
LOGIN_REDIRECT_URL = '/'
REGISTRATION_EMAIL_REGISTER_SUCCESS_URL = '/account/'

#django-social-auth
AUTHENTICATION_BACKENDS = (

    'social_auth.backends.contrib.vkontakte.VKontakteOAuth2Backend',
    'social_auth.backends.contrib.github.GithubBackend',

    'django.contrib.auth.backends.ModelBackend',
    'registration_email.auth.EmailBackend',
)


GITHUB_APP_ID = '509bfa9805b9a0bd5e4c'
GITHUB_API_SECRET = 'dcc12daff5dcc0a00c68a726c4475f49971336f2'
TWITTER_CONSUMER_KEY         = ''
TWITTER_CONSUMER_SECRET      = ''
FACEBOOK_APP_ID              = ''
FACEBOOK_API_SECRET          = ''
LINKEDIN_CONSUMER_KEY        = ''
LINKEDIN_CONSUMER_SECRET     = ''
ORKUT_CONSUMER_KEY           = ''
ORKUT_CONSUMER_SECRET        = ''
GOOGLE_CONSUMER_KEY          = ''
GOOGLE_CONSUMER_SECRET       = ''
GOOGLE_OAUTH2_CLIENT_ID      = ''
GOOGLE_OAUTH2_CLIENT_SECRET  = ''
FOURSQUARE_CONSUMER_KEY      = ''
FOURSQUARE_CONSUMER_SECRET   = ''
VK_APP_ID                    = '3533798'
VK_API_SECRET                = 'KFaq7MhImgNSnjzRkktO'
LIVE_CLIENT_ID               = ''
LIVE_CLIENT_SECRET           = ''
SKYROCK_CONSUMER_KEY         = ''
SKYROCK_CONSUMER_SECRET      = ''
YAHOO_CONSUMER_KEY           = ''
YAHOO_CONSUMER_SECRET        = ''
READABILITY_CONSUMER_SECRET  = ''
READABILITY_CONSUMER_SECRET  = ''

LOGIN_URL          = '/accounts/login/'
LOGIN_REDIRECT_URL = '/'
LOGIN_ERROR_URL    = '/accounts/login-error/'


VKONTAKTE_APP_AUTH = {
    'key':  'duZcjJzZ5643t4WluAxu',
    'user_mode': 2,
    'id': '3532966'
}
VKONTAKTE_OAUTH2_EXTRA_SCOPE = ['notify', 'friends', 'photos', 'status', 'wall', 'nohttps']


if os.environ.get('django_local', 0):
    DEBUG = True
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
            'NAME': 'base.db',                      # Or path to database file if using sqlite3.
            # The following settings are not used with sqlite3:
            'USER': '',
            'PASSWORD': '',
            'HOST': '',                      # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
            'PORT': '',                      # Set to empty string for default.
        }
    }

    MEDIA_ROOT = os.path.join(os.path.dirname(__file__), '..', 'media')

    STATIC_ROOT = os.path.join(os.path.dirname(__file__), '..', 'static')

    STATIC_URL = 'http://127.0.0.1:8000/static/'
    MEDIA_URL = 'http://127.0.0.1:8000/media/'


# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}
