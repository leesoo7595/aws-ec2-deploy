from .base import *

secret = json.load(open(os.path.join(SECRETS_DIR, 'dev.json')))

DEBUG = True

# django-storages
INSTALLED_APPS += [
    'storages',
]
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
AWS_ACCESS_KEY_ID = secret['AWS_ACCESS_KEY_ID']
AWS_SECRET_ACCESS_KEY = secret['AWS_SECRET_ACCESS_KEY']
AWS_STORAGE_BUCKET_NAME = secret['AWS_STORAGE_BUCKET_NAME']
AWS_DEFAULT_ACL = secret['AWS_DEFAULT_ACL']
AWS_S3_REGION_NAME = secret['AWS_S3_REGION_NAME']
AWS_S3_SIGNATURE_VERSION = secret['AWS_S3_SIGNATURE_VERSION']

# Static
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(ROOT_DIR, '.static')

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(ROOT_DIR, '.media')

# WSGI
WSGI_APPLICATION = 'config.wsgi.dev.application'

# DB
DATABASES = secret['DATABASES']