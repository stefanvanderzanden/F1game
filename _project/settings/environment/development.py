from _project.settings.base import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'f1game',
        'USER': 'f1game',
        'PASSWORD': 'f1game',
        'HOST': 'db',
        'PORT': 5432,
    }
}