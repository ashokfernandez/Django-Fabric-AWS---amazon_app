from amazon_app.settings.common import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'mytestdb',
		'USER' : 'testadmin',
		'PASSWORD' : 'mircosoft1',
        'HOST' : 'mytestdbinstance.cz4efotqc3jm.ap-southeast-2.rds.amazonaws.com',
        'PORT' : '5432',
    }
}

# Static files via Amazon S3 (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

INSTALLED_APPS += ('storages',)
AWS_STORAGE_BUCKET_NAME = "myamazontestapp-static"
STATICFILES_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
S3_URL = 'http://%s.s3.amazonaws.com/' % AWS_STORAGE_BUCKET_NAME
STATIC_URL = S3_URL
