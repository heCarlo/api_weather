from datetime import timedelta
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-x*(q3p^1)e-&sa@q89judj%=or7f8bht7xr)!qh5ppi*d*345j'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework_simplejwt',
    'rest_framework',
    'weather',
    'user',
]
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
}

# Configurações específicas para o Simple JWT
SIMPLE_JWT = {
    # Define o tempo de expiração do token de acesso (em minutos)
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=15),
    # Define o tempo de expiração do token de atualização (em dias)
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
    # Configura a chave secreta para assinar os tokens
    'SIGNING_KEY': '1234',
    # Configura se os tokens devem ser codificados usando a compactação JWT
    'ALGORITHM': 'HS256',
    # Configura se os tokens devem ser encriptados
    'AUTH_HEADER_TYPES': ('Bearer',),
    # Configura se o usuário deve ter um identificador exclusivo no token
    'USER_ID_FIELD': 'uuid',
    # Configura se o token deve incluir informações do usuário
    'USER_ID_CLAIM': 'uuid',
    # Configura se o token deve incluir informações do usuário
    'USER_ID_CLAIM': 'uuid',
    # Configura se o token deve incluir informações do usuário
    'AUTH_TOKEN_CLASSES': ('rest_framework_simplejwt.tokens.AccessToken',),
}


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware'
]

ROOT_URLCONF = 'core.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            BASE_DIR / 'templates'
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

WSGI_APPLICATION = 'core.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases


# MONGO_CONNECTION_STRING = 'mongodb+srv://carlosgfkp:123@cluster0.cqoroep.mongodb.net/'
MONGO_CONNECTION_STRING = 'mongodb://localhost:27017'
MONGO_DATABASE_NAME = 'weather'

DATABASES = {
    'default': {
        'ENGINE': 'djongo',
        'ENFORCE_SCHEMA': True,
        'NAME': MONGO_DATABASE_NAME,
        'CLIENT': {
            'host': MONGO_CONNECTION_STRING,
            # 'username': 'carlosgfkp',
            # 'password': '123',
        }
    }
}



# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
