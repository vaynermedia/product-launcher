# Django settings for snowboard project.
import django
import os
import sys

DEBUG = __DEBUG__
TEMPLATE_DEBUG = '__TEMPLATE_DEBUG__'
SPRINTLY_ENV = os.getenv('LAUNCHPAD_ENV', 'DEVELOPMENT')

ADMINS = (
    ('Joe Stump', 'joe@joestump.net'),
)

# Set up our paths
SITE_ROOT = os.path.dirname(os.path.realpath(`__file__'))
sys.path.insert(0, "%s%sapps" % (SITE_ROOT, os.sep))
sys.path.insert(0, "%s%ssite-packages" % (SITE_ROOT, os.sep))

MANAGERS = ADMINS

# Use DATABASES for Django >= 1.2 (and to avoid deprecation
# warnings when >= 1.3
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.__DATABASE_ENGINE__',
        'NAME': __DATABASE_NAME__,
        'USER': '__DATABASE_USER__',
        'PASSWORD': '__DATABASE_PASSWORD__',
        'HOST': '__DATABASE_HOST__',
        'PORT': '__DATABASE_PORT__'
    }
}

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'America/Los_Angeles'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT = ''

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
MEDIA_URL = ''

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_PREFIX = '/media/'

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'feuq35c6-!u0z)fal-5viac@hj$za^egrp=@c=3i9uyl4%r_c$'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.load_template_source',
)

TEMPLATE_DIRS = (
    '%s/templates' % SITE_ROOT
)

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.contrib.messages.context_processors.messages",
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)

ROOT_URLCONF = 'urls'

MESSAGE_STORAGE = 'django.contrib.messages.storage.session.SessionStorage'

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.admindocs',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'taggit',
    'south',
    'gravatar',
    'django_jenkins',
    'ajax',
)

# Default From header for outbound emails
DEFAULT_FROM_EMAIL = '__DEFAULT_FROM_EMAIL__'

# Email settings
if SPRINTLY_ENV == 'DEVELOPMENT':
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
else:
    EMAIL_HOST_USER = '__EMAIL_HOST_USER__'
    EMAIL_HOST_PASSWORD = '__EMAIL_HOST_PASSWORD__'
    EMAIL_HOST = '__EMAIL_HOST__'
    EMAIL_PORT = __EMAIL_PORT__

# The URI for the login page.
LOGIN_URL = '/account/login/'

# Default of where to redirect after a login.
LOGIN_REDIRECT_URL = '/'

# Our session's cookie name
SESSION_COOKIE_NAME = 'launcher'

# Needed to keep tests from borking.
SOUTH_TESTS_MIGRATE = False

# Only run Jenkins report generation on these apps.
PROJECT_APPS = ('wasatch', 'accounts',)

# Which Jenkins reports/tasks to run.
JENKINS_TASKS = ('django_jenkins.tasks.run_pep8',
                 'django_jenkins.tasks.run_pyflakes',
                 'django_jenkins.tasks.with_coverage',
                 'django_jenkins.tasks.django_tests',)

# The test runner for the Jenkins command.
JENKINS_TEST_RUNNER = 'django_jenkins.runner.CITestSuiteRunner'

# Don't send 404 emails.
SEND_BROKEN_LINK_EMAILS = False

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '[%(asctime)s] %(levelname)s %(name)s - %(message)s'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler'
        },
        'snowbird': {
            'level': '__LOG_LEVEL__',
            'class': 'logging.FileHandler',
            'formatter': 'verbose',
            'filename': '__LOG_FILE__'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
        'snowbird.apps.wasatch.views': {
            'handlers': ['snowbird'],
            'level': '__LOG_LEVEL__'
        },
        'snowbird.apps.accounts.views': {
            'handlers': ['snowbird'],
            'level': '__LOG_LEVEL__'
        },
        'snowbird.apps.api.views': {
            'handlers': ['snowbird'],
            'level': '__LOG_LEVEL__'
        }
    }
}
