"""
Django settings for reborn project.

Generated by 'django-admin startproject' using Django 4.0.3.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""
from datetime import timedelta
from pathlib import Path
import os
import dj_database_url


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# BASE_DIR = Path(__file__).resolve().parent.parent
# BASE_PARENT_DIR = Path(__file__).resolve().parent.parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', 'django-insecure-c9nlv4wnbum#)3r#1_42xy@fye%fw!j6erk#9eqn*v53y80&g#')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# # SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY = 'django-insecure-c9nlv4wnbum#)3r#1_42xy@fye%fw!j6erk#9eqn*v53y80&g#'

# # SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = True

ALLOWED_HOSTS = ['connectbill.herokuapp.com']


# Application definition

INSTALLED_APPS = [
    'corsheaders',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
#   'django.contrib.staticfiles',
    
    'portfolio',
# portfolio Application connected
    'users',
# users app connected
    'userReview',
# customerReview connected
    'client_commission',
# client_commission app is connected
    'Mypage',
# Mypage App is connected    

#   'django_crontab',
    'rest_framework.authtoken',
    'rest_framework',
    

]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware'
]

CORS_ORIGIN_WHITELIST = [
    'http://127.0.0.1:3000' ,'http://localhost:3000',
    'http://127.0.0.1:8000' ,'http://localhost:8000',
    'https://connectbill-frontend-soongsil.vercel.app',
]
CORS_ALLOW_CREDENTIALS = True


# CORS_ALLOWED_ORIGINS = [
#     'https://connectbill-frontend-soongsil.vercel.app',
# ]


ROOT_URLCONF = 'reborn.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            'templates',
        ],
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

WSGI_APPLICATION = 'reborn.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME':  os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
db_from_env = dj_database_url.config(conn_max_age=500)
DATABASES['default'].update(db_from_env)


# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

# STATIC_URL = 'static/'

# STATICFILES_DIRS = [
#     #BASE_DIR / 'static',
#     os.path.join(BASE_PARENT_DIR,'frontend/build/static'),  

# ]

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'



REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.TokenAuthentication',
    ],
    # 'DEFAULT_RENDERER_CLASSES': [
    #     'rest_framework.renderers.JSONRenderer',
    # ],
    # 'DEFAULT_PARSER_CLASSES': [
    #     'rest_framework.parsers.JSONParser',
    #     'rest_framework.parsers.FormParser',
    #     'rest_framework.parsers.MultiPartParser'
    # ]
}
AUTH_USER_MODEL = 'users.User'

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
# AWS_S3_SECURE_URLS = False       # use http instead of https
# AWS_QUERYSTRING_AUTH = False     # don't add complex authentication-related query parameters for requests

ACCOUNT_LOGOUT_ON_GET = True

# 로그인 성공후 이동하는 URL
LOGIN_REDIRECT_URL = '/'

# 로그아웃시 이동하는 URL
LOGOUT_REDIRECT_URL = '/'


CRONJOBS = [
    ('* 0 * * *','reborn.cron.changeStatus','>> schedule.log')
]

SIMPLE_JWT = {
  'ACCESS_TOKEN_LIFETIME': timedelta(minutes=5),
  'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
  'ROTATE_REFRESH_TOKENS': False,
  'BLACKLIST_AFTER_ROTATION': True,
  'UPDATE_LAST_LOGIN': False,

  'ALGORITHM': 'HS256',
  'SIGNING_KEY': SECRET_KEY,
  'VERIFYING_KEY': None,
  'AUDIENCE': None,
  'ISSUER': None,

  'AUTH_HEADER_TYPES': ('Bearer',),
  'AUTH_HEADER_NAME': 'HTTP_AUTHORIZATION',
  'USER_ID_FIELD': 'id',
  'USER_ID_CLAIM': 'user_id',
  'USER_AUTHENTICATION_RULE': 'rest_framework_simplejwt.authentication.default_user_authentication_rule',

  'AUTH_TOKEN_CLASSES': ('rest_framework_simplejwt.tokens.AccessToken',),
  'TOKEN_TYPE_CLAIM': 'token_type',

  'JTI_CLAIM': 'jti',

  'SLIDING_TOKEN_REFRESH_EXP_CLAIM': 'refresh_exp',
  'SLIDING_TOKEN_LIFETIME': timedelta(minutes=5),
  'SLIDING_TOKEN_REFRESH_LIFETIME': timedelta(days=1),

  # custom
  'AUTH_COOKIE': 'access_token',  # Cookie name. Enables cookies if value is set.
  'AUTH_COOKIE_DOMAIN': None,     # A string like "example.com", or None for standard domain cookie.
  'AUTH_COOKIE_SECURE': False,    # Whether the auth cookies should be secure (https:// only).
  'AUTH_COOKIE_HTTP_ONLY' : True, # Http only cookie flag.It's not fetch by javascript.
  'AUTH_COOKIE_PATH': '/',        # The path of the auth cookie.
  'AUTH_COOKIE_SAMESITE': 'Lax',  # Whether to set the flag restricting cookie leaks on cross-site requests. This can be 'Lax', 'Strict', or None to disable the flag.
}




STATICFILES_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'

STATIC_URL = 'http://bucketforconnectbill.s3.amazonaws.com/'
ADMIN_MEDIA_PREFIX = STATIC_URL + 'admin/'


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

# The absolute path to the directory where collectstatic will collect static files for deployment.
# STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# # The URL to use when referring to static files (where they will be served from)
# STATIC_URL = '/static/'
