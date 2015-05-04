DEFAULT_CHARSET = 'utf-8'

TIME_ZONE = 'Europe/Moscow'

LANGUAGE_CODE = 'en'

SITE_ID = 1

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
    'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'kiuss.urls'

WSGI_APPLICATION = 'kiuss.wsgi.application'

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'south',
    'easy_thumbnails',
    'artworks',
    'django.contrib.admin',
)

THUMBNAIL_QUALITY = 90

THUMBNAIL_ALIASES = {
    '': {
        '100px': {
            'size': (100, 100),
            'crop': True,
            'progressive': True,
        },
        '200px': {
            'size': (200, 200),
            'crop': True,
            'progressive': True,
        },
        '200pxw': {
            'size': (200, 0),
            'crop': True,
            'progressive': True,
        },
        '300px': {
            'size': (300, 300),
            'crop': True,
            'progressive': True,
        },
        '400px': {
            'size': (400, 400),
            'crop': True,
            'progressive': True,
        },
        '400pxw': {
            'size': (400, 0),
            'crop': True,
            'progressive': True,
        },
        '800px': {
            'size': (800, 800),
            'crop': True,
            'progressive': True,
        },
        '800pxw': {
            'size': (800, 0),
            'crop': True,
            'progressive': True,
        },
        '1400pxw': {
            'size': (1400, 0),
            'crop': True,
            'progressive': True,
        },
        'w100h200': {
            'size': (100, 200),
            'crop': True,
            'progressive': True,
        },
        'w200h100': {
            'size': (200, 100),
            'crop': True,
            'progressive': True,
        },
        'w200h400': {
            'size': (200, 400),
            'crop': True,
            'progressive': True,
        },
        'w400h200': {
            'size': (400, 200),
            'crop': True,
            'progressive': True,
        },
    },
}

SOUTH_MIGRATION_MODULES = {
    'easy_thumbnails': 'easy_thumbnails.south_migrations',
}

SESSION_SERIALIZER = 'django.contrib.sessions.serializers.JSONSerializer'

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

try:
    from local_settings import *
except ImportError:
    pass
