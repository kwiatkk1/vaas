# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

import os
from django.conf import global_settings
from vaas.configuration.loader import YamlConfigLoader

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
current_dir = os.path.abspath(os.path.dirname(__file__))
config_loader = YamlConfigLoader()

if not config_loader.determine_config_file('db_config.yml'):
    raise EnvironmentError('Cannot find db_config file')

DATABASES = config_loader.get_config_tree('db_config.yml')

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'pwm_&@a%yd8+7mqf9=*l56+y!@sb7ab==g942j7++gnr9l2%*d'

# SECURITY WARNING: don't run with debug turned on in production!
ALLOWED_HOSTS = []

MESSAGE_STORAGE = 'django.contrib.messages.storage.session.SessionStorage'

# Application definition
INSTALLED_APPS = (
    'django_nose',
    'vaas.adminext',
    'material',
    'material.frontend',
    'material.admin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'tastypie',
    'simple_history',
    'vaas.manager',
    'vaas.cluster',
    'vaas.monitor',
    'vaas.account',
    'vaas.purger',
    'taggit',
    'django_ace',
)

MIDDLEWARE_CLASSES = (
    'djangosecure.middleware.SecurityMiddleware',
    'log_request_id.middleware.RequestIDMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'vaas.manager.middleware.VclRefreshMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'simple_history.middleware.HistoryRequestMiddleware',
)

SECURE_CONTENT_TYPE_NOSNIFF = True

ROOT_URLCONF = 'vaas.urls'

WSGI_APPLICATION = 'vaas.external.wsgi.application'

SIGNALS = 'on'

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Europe/Warsaw'
USE_I18N = True
USE_L10N = True
USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, "static/")

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            current_dir + "templates",
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                # Insert your TEMPLATE_CONTEXT_PROCESSORS here or use this
                # list if you haven't customized them:
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.debug',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.tz',
                'django.contrib.messages.context_processors.messages',
            ]
        }
    }
]

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
        },
    },
    'handlers': {
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': '/tmp/debug.log',
            'formatter': 'verbose'
        },
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['file', 'console'],
            'propagate': False,
            'level': 'DEBUG',
        },
        'vaas': {
            'handlers': ['file', 'console'],
            'propagate': False,
            'level': 'DEBUG',
        },
        '': {
            'handlers': ['file', 'console'],
            'level': 'DEBUG',
        }
    }
}

VAAS_LOADER_PARTIAL_RELOAD = False
VAAS_LOADER_MAX_WORKERS = 30

REFRESH_TRIGGERS_CLASS = (
    'Probe', 'Backend', 'Director', 'VarnishServer', 'VclTemplate', 'VclTemplateBlock', 'TimeProfile'
)

# CELERY
BROKER_URL = 'redis://localhost:6379/1'
CELERY_RESULT_BACKEND = 'redis://localhost:6379/2'
CELERY_TASK_RESULT_EXPIRES = 600
CELERY_TASK_SERIALIZER = 'pickle'
CELERY_RESULT_SERIALIZER = 'pickle'
CELERY_IGNORE_RESULT = False
CELERY_TASK_PUBLISH_RETRY = True


VARNISH_COMMAND_TIMEOUT = 5
