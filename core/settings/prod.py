import os

from .base import *

DEBUG = True
ALLOWED_HOSTS = ['biblio.framanmag.com', 'webbiblio.herokuapp.com']

DB_HOST = os.environ["DB_HOST"]
DB_NAME = os.environ["DB_NAME"]
DB_PASS = os.environ["DB_PASS"]
DB_USER = os.environ["DB_USER"]
SECRET_KEY = os.environ["SECRET_KEY"]

MEDIA_URL = '/media/'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': DB_NAME,
        'HOST': DB_HOST,
        'PORT': 5432,
        'USER': DB_USER,
        'PASSWORD': DB_PASS
    }
}
