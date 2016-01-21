
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = '=8t$@6645h!mpevbd5+zlbv#w&cfhxv7285sa27vj_#&ojcci&'

DEBUG = True
LOCAL = True

ALLOWED_HOSTS = []

# Application definition
INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> 7125d6b40bc7986e6e6b750b19bd01eb326a8371

    #Our apps
    'login',
    'projects'
<<<<<<< HEAD
=======
>>>>>>> 08e6daf952d94e00aac05a7072854cc29a5725a0
>>>>>>> 7125d6b40bc7986e6e6b750b19bd01eb326a8371
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'omaha.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR,'templates'),
            os.path.join(BASE_DIR,'omaha/templates'),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.template.context_processors.static',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'omaha.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'omaha',
        'USER': 'root',
        'PASSWORD': 'ventamovil'
    }
}

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")
STATIC_URL = '/static/'
<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> 7125d6b40bc7986e6e6b750b19bd01eb326a8371

MEDIA_ROOT = os.path.join(BASE_DIR, "staticfiles/media")
MEDIA_URL = '/static/media/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"),
)
if LOCAL:
    try:
        from local_settings import *
    except Exception, e:
<<<<<<< HEAD
                e
=======
=======
if LOCAL:
    try:
        from local_settings import *
    except Exception ,e:
>>>>>>> 08e6daf952d94e00aac05a7072854cc29a5725a0
        raise e
>>>>>>> 7125d6b40bc7986e6e6b750b19bd01eb326a8371
