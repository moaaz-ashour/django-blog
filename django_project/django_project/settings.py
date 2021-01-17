"""
Django settings for django_project project.

Generated by 'django-admin startproject' using Django 3.1.4.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

import os
import django_on_heroku
from pathlib import Path
from django.urls import reverse_lazy
from dotenv import load_dotenv
load_dotenv()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = str(os.getenv('SECRET_KEY'))

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = (str(os.getenv('DEBUG_VALUE')) == 'True') # value as bool.

ALLOWED_HOSTS = []


# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MY_APPS = [
    'blog.apps.BlogConfig',
    'users.apps.UsersConfig',
    'crispy_forms',
    'django_cleanup',
    'storages'
]

INSTALLED_APPS.extend(MY_APPS)



MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'django_project.urls'

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

WSGI_APPLICATION = 'django_project.wsgi.application'


# Database ( for development )
# For deployment, we use Postgres. 
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles') # for static files (Heroku)

MEDIA_ROOT = os.path.join(BASE_DIR, 'media') # full Path to where you want Django to save uploaded files.
MEDIA_URL = '/media/'  # public URL of MEDIA_ROOT directory

# for django-crispy-forms=
CRISPY_TEMPLATE_PACK = 'bootstrap4'

# Login URL and redirection
LOGIN_REDIRECT_URL = 'blog-home'
LOGIN_URL = reverse_lazy('login')

# SMTP Configs:
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = str(os.getenv('EMAIL_USER'))
EMAIL_HOST_PASSWORD = str(os.getenv('EMAIL_PASSWORD'))


# Django Storages settings to upload media files to S3.
# S3 BUCKET CONFIG
# https://django-storages.readthedocs.io/en/latest/backends/amazon-S3.html
AWS_ACCESS_KEY_ID = str(os.getenv("AWS_ACCESS_KEY_ID"))
AWS_SECRET_ACCESS_KEY = str(os.getenv("AWS_SECRET_ACCESS_KEY"))
AWS_STORAGE_BUCKET_NAME = cstr(os.getenv("AWS_STORAGE_BUCKET_NAME"))

AWS_S3_FILE_OVERWRITE = False
AWS_DEFAULT_ACL = None # default is None which means the file will inherit the bucket's permission

DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'