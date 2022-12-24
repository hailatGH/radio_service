import os
import django
from django.utils.encoding import force_str
from urllib.parse import urlparse

from dotenv import load_dotenv
from .basesettings import *


django.utils.encoding.force_text = force_str
load_dotenv()

if os.getenv('ENV') == "ENV":
    DEBUG = True

SECRET_KEY = (str, os.getenv("SECRET_KEY"))
URL = os.getenv('URL')


if URL:
    ALLOWED_HOSTS = [urlparse(URL).netloc]
    CSRF_TRUSTED_ORIGINS = [URL]
else:
    ALLOWED_HOSTS = ["*"]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': "radio_database",
        'USER': "zemadatabaseadmin",
        'PASSWORD': "StrongP@ssword",
        'HOST': "zema-postgresql-v100.postgres.database.azure.com",
        'PORT': '5432',
        'OPTIONS': {'sslmode': 'disable'}
    }
}

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, '/static/'),
]
AZURE_ACCOUNT_NAME = 'zemastroragev100'
AZURE_ACCOUNT_KEY = 'AFsY2hZVbyYBKisEkRL+toNNJ7yBOzoJ/cruOxurFHnU84vE+Cmloq9S2ZkCxYaxrM5QemPsUiX5+ASt4WEg8w=='
AZURE_CUSTOM_DOMAIN = f'{AZURE_ACCOUNT_NAME}.blob.core.windows.net'
AZURE_LOCATION = 'zemacontainer'
AZURE_CONTAINER = 'zemacontainer'

STATIC_LOCATION = 'static'
STATIC_URL = f'https://{AZURE_CUSTOM_DOMAIN}/{STATIC_LOCATION}/'

STATICFILES_STORAGE = 'storages.backends.azure_storage.AzureStorage'
DEFAULT_FILE_STORAGE = 'core.custom_storage.AzureMediaStorage'
