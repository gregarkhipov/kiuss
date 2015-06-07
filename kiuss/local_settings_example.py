import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

SECRET_KEY = 'df6b8j1h6s45d23l5f16bj85h1a32l5s1d52f54k1012v5j65h46vh'

#DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'kiuss.sqlite3'),
    }
}

ALLOWED_HOSTS = [
    'kiusscollective.pl',
    'www.kiusscollective.pl',
]
