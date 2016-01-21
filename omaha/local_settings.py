<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> 7125d6b40bc7986e6e6b750b19bd01eb326a8371
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

STATIC_ROOT = os.path.join(BASE_DIR, "../static")
MEDIA_ROOT = os.path.join(BASE_DIR, "../static/media")

# TAE_URL = "http://evm.ventamovil.com.mx:9094/service.asmx?WSDL"
# TAE_URL = 'http://10.10.10.11:9109/service.asmx?WSDL'

STATIC_URL = '/static/'
MEDIA_URL = '/media/'
<<<<<<< HEAD
=======

=======
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

STATIC_ROOT = os.path.join(BASE_DIR, "../static")
MEDIA_ROOT = os.path.join(BASE_DIR, "../static/media")

# TAE_URL = "http://evm.ventamovil.com.mx:9094/service.asmx?WSDL"
# TAE_URL = 'http://10.10.10.11:9109/service.asmx?WSDL'

STATIC_URL = '/static/'
MEDIA_URL = '/media/'

>>>>>>> 08e6daf952d94e00aac05a7072854cc29a5725a0
>>>>>>> 7125d6b40bc7986e6e6b750b19bd01eb326a8371
