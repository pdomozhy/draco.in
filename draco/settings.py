"""
Django settings for draco project.

Generated by 'django-admin startproject' using Django 2.0.9.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '%q1zi1$62$5tlnye+w=m)0j!w2x=r*#**d0(a-)h-gh^ppcilw'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['localhost', '192.168.8.214']


# Application definition

INSTALLED_APPS = [
    # 'dracoin.apps.DracoinConfig',
    'tinymce',
    'dracoin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'draco.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates/')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.media',
            ],
        },
    },
]

WSGI_APPLICATION = 'draco.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Europe/Kiev'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static/')]

# Mediafiles (Images, etc.)
MEDIA_ROOT = os.path.join(BASE_DIR, 'upload/')
MEDIA_URL = '/upload/'


# TinyMCE configuration
TINYMCE_DEFAULT_CONFIG = {
    'content_css': 'https://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/css/bootstrap.min.css',
    'height': 360,
    # 'toolbar': 'codesample',
    # 'toolbar': 'newdocument, undo, redo, visualaid, cut, copy, paste, selectall, bold, italic, underline, strikethrough, subscript, superscript, removeformat, formats',
    'plugins': [
      'advlist autolink link image lists charmap print preview hr anchor pagebreak spellchecker',
      'searchreplace wordcount visualblocks visualchars code fullscreen insertdatetime media nonbreaking',
      'save table contextmenu directionality emoticons template paste textcolor', 'codesample',
    ],
    'toolbar': 'insertfile undo redo | styleselect | bold italic | alignleft aligncenter alignright alignjustify | bullist numlist outdent indent | link image | print preview media fullpage | forecolor backcolor emoticons | codesample'
    # 'codesample_languages': [
    #     {'text': 'HTML/XML', 'value': 'markup'},
    #     {'text': 'JavaScript', 'value': 'javascript'},
    #     {'text': 'CSS', 'value': 'css'},
    #     {'text': 'Python', 'value': 'python'},
    #     {'text': 'C', 'value': 'c'},
    #     {'text': 'C++', 'value': 'cpp'},
    #     {'text': 'Arduino', 'value': 'arduino'},
    #     {'text': 'Diff', 'value': 'diff'},
    #     {'text': 'Django/Jinja2', 'value': 'django'},
    #     {'text': 'Docker', 'value': 'docker'},
    #     {'text': 'Git', 'value': 'git'},
    #     {'text': 'SQL', 'value': 'sql'},
    #     {'text': 'Makefile', 'value': 'makefile'},
    #     {'text': 'Markdown', 'value': 'markdown'},
    #     {'text': 'Haskell', 'value': 'haskell'},
    #     {'text': 'LaTeX', 'value': 'latex'},
    #     {'text': 'JSON+JSONP', 'value': 'json'},
    # ],
        # JavaScript
        # Markup + HTML + XML + SVG + MathML
        # Arduino
        # Bash + Shell
        # C
        # C++
        # Diff
        # Django/Jinja2
        # Docker
        # Git
        # vim
        # SQL
        # Makefile
        # Markdown
        # LaTeX
        # JSON + JSONP
        # Python
        # Haskell
}


# Email settings SMTP:

EMAIL_HOST = 'localhost'
EMAIL_PORT = 1025

# Email for debug:
# EMAIL_HOST = 'localhost'
# EMAIL_PORT = 1025
# #use:
# python -m smtpd -n -c DebuggingServer localhost:1025