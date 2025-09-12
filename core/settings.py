

from pathlib import Path
import os





# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure--ku^7@-2&v3@xgm95+82l4)nq++^ocw7m4&_c8k07(i2bl567+'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    "jazzmin", 
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # local apps
    'users',
    'courses',
    'home',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    # 'users.middleware.ProfileCompletionMiddleware',

]

ROOT_URLCONF = 'core.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            BASE_DIR / 'templates',
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'core.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.2/ref/settings/#auth-password-validators

AUTH_USER_MODEL = 'users.CustomUser'


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
# https://docs.djangoproject.com/en/5.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True



# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.2/howto/static-files/

STATIC_URL = 'static/'
STATICFILES_DIRS = [
    BASE_DIR / 'static'
]


MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media-files"


# Default primary key field type
# https://docs.djangoproject.com/en/5.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'









JAZZMIN_SETTINGS = {
    "site_title": "ItCourse Admin",
    "site_header": "ItCourse Panel",
    "site_brand": "ItCourse",
    "welcome_sign": "Xush kelibsiz ItCourse Admin paneliga",
    "copyright": "ItCourse",
    "show_sidebar": True,
    "navigation_expanded": True,
    "topmenu_links": [
        {"name": "Bosh sahifa", "url": "admin:index", "permissions": ["auth.view_user"]},
        {"model": "auth.User"},
        {"model": "yourapp.Course"},
    ],
    "icons": {
        "auth.User": "fas fa-user",
        "auth.Group": "fas fa-users",
        "yourapp.Course": "fas fa-book",
        "yourapp.Module": "fas fa-layer-group",
        "yourapp.Video": "fas fa-video",
    },
}

JAZZMIN_UI_TWEAKS = {
    "theme": "cosmo",           # bootstrap temasi (cosmo, litera, lumen va hok.)
    "dark_mode_theme": "darkly",
    "navbar": "navbar-dark navbar-primary",
    "sidebar": "sidebar-dark-primary",
    "brand_colour": "navbar-primary",
    "accent": "accent-info",
    "body_small_text": False,
    "sidebar_fixed": True,
    "navbar_fixed": True,
    "footer_fixed": False,
}
