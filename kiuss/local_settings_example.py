#DEBUG = True
#TEMPLATE_DEBUG = DEBUG

import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))


ADMINS = (
    ('John Appleseed', 'john@me.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'kiuss',
        'USER': 'john',
        'PASSWORD': 'lk23h48e5v',
        'HOST': 'localhost',
        'PORT': '',
    }
}

ALLOWED_HOSTS = [
    'kiusscollective.com',
    'kiusscollective.fr',
]

SECRET_KEY = 'sd5f1g4r3s6a34d6g1l346if64316dghj'

MEDIA_ROOT = os.path.abspath(os.path.join(BASE_DIR, 'media'))

MEDIA_URL = '/media/'

STATIC_ROOT = os.path.abspath(os.path.join(BASE_DIR, 'static'))

STATIC_URL = '/static/'

STATICFILES_DIRS = (
    (STATIC_ROOT,),
)

TEMPLATE_DIRS = (
    os.path.abspath(os.path.join(BASE_DIR, 'templates')),
)
