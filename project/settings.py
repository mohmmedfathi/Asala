import os
from pathlib import Path
from datetime import timedelta
import dj_database_url

BASE_DIR = Path(__file__).resolve().parent.parent


SECRET_KEY = 'django-insecure-g^+e0kq6x-sy@=hwwe9vu4^at&puk^_1%q#43o=v*1er6-9qv)'

DEBUG = True

if not DEBUG:
    STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles') 
    STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

ALLOWED_HOSTS = ["https://asala.onrender.com","www.asala.onrender.com","*"]


INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    'rest_framework',
    'rest_framework_simplejwt',
    'corsheaders',
    'drf_yasg',
    
    'accounts',
    'communities',
    'clubs',
    'category',
    'products',
    'search',
    'recommendations',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'project.wsgi.application'


# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }
# postgresql://asala_postgres_user:wv209HQOYUTr7MDKClmIcq9N68xrO3sc@dpg-cvfi5t5umphs73daajh0-a.oregon-postgres.render.com/asala_postgres
DATABASES = {
    'default': dj_database_url.config(
        default='postgresql://asala_postgres_user:wv209HQOYUTr7MDKClmIcq9N68xrO3sc@dpg-cvfi5t5umphs73daajh0-a.oregon-postgres.render.com/asala_postgres',
        conn_max_age=600
    )
}
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': 'asala_postgres',
#         'USER': 'asala_postgres_user',
#         'PASSWORD': 'wv209HQOYUTr7MDKClmIcq9N68xrO3sc',
#         'HOST': 'postgresql://asala_postgres_user:wv209HQOYUTr7MDKClmIcq9N68xrO3sc@dpg-cvfi5t5umphs73daajh0-a.oregon-postgres.render.com/asala_postgres',
#         'PORT': '5432',
#     }
# }

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]



LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True



STATIC_URL = '/static/'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

AUTH_USER_MODEL = 'accounts.CustomUser'

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    )
}

CORS_ALLOW_ALL_ORIGINS = True  
CORS_ALLOW_CREDENTIALS = True  

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=4),  
    'REFRESH_TOKEN_LIFETIME': timedelta(days=7),  
    'ROTATE_REFRESH_TOKENS': False,
    'BLACKLIST_AFTER_ROTATION': True,
    'ALGORITHM': 'HS256',
    'SIGNING_KEY': SECRET_KEY,
    'AUTH_HEADER_TYPES': ('Bearer',),
    'USER_ID_FIELD': 'id',
    'USER_ID_CLAIM': 'user_id',
}

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'
