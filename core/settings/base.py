from pathlib import Path
from django.utils.translation import gettext_lazy as _
import environ

env = environ.Env(DEBUG=(bool, False))
BASE_DIR = Path(__file__).resolve().parent.parent.parent
environ.Env.read_env(BASE_DIR / ".env")

SECRET_KEY = env("SECRET_KEY")

DEBUG = env("DEBUG")

ALLOWED_HOSTS = env("ALLOWED_HOSTS").split(" ")

# Application definition
DJANGO_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]

LOCAL_APPS = [
    "shop.apps.ShopConfig",
    "cart.apps.CartConfig",
    "orders.apps.OrdersConfig",
    "payment.apps.PaymentConfig",
    "coupons.apps.CouponsConfig",
]

THIRD_PARTY_APPS = [
    "rosetta",
    "parler",
    "localflavor",
]

INSTALLED_APPS = DJANGO_APPS + LOCAL_APPS + THIRD_PARTY_APPS

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.locale.LocaleMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "core.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "cart.context_processors.cart",
            ],
        },
    },
]

WSGI_APPLICATION = "core.wsgi.application"


AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


LANGUAGE_CODE = "en"

LANGUAGES = [
    ("en", _("English")),
    ("es", _("Spanish")),
]

LOCALE_PATHS = [
    BASE_DIR / "locale",
]

TIME_ZONE = "Africa/Lagos"

USE_I18N = True

USE_TZ = True


STATIC_URL = "static/"
STATIC_ROOT = "/static/"


STATICFILES_FINDERS = (
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
)

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


MEDIA_URL = "media/"
MEDIA_ROOT = "/media/"


CART_SESSION_ID = "cart"


EMAIL_BACKEND = env("EMAIL_BACKEND")


# Stripe settings
STRIPE_PUBLISHABLE_KEY = env("STRIPE_PUBLISHABLE_KEY")  # Publishable key
STRIPE_SECRET_KEY = env("STRIPE_SECRET_KEY")  # Secret key
STRIPE_API_VERSION = env("STRIPE_API_VERSION")
STRIPE_WEBHOOK_SECRET = env("STRIPE_WEBHOOK_SECRET")


# Redis settings
REDIS_HOST = env("REDIS_HOST")
REDIS_PORT = env("REDIS_PORT")
REDIS_DB = env("REDIS_DB")


# CELERY
CELERY_BROKER_URL = env("CELERY_BROKER")
CELERY_RESULT_BACKEND = env("CELERY_BACKEND")
CELERY_ACCEPT_CONTENT = ["application/json"]
CELERY_TASK_SERIALIZER = "json"
CELERY_RESULT_SERIALIZER = "json"
CELERY_TIMEZONE = "Africa/Lagos"


# django-parler settings
PARLER_LANGUAGES = {
    None: (
        {"code": "en"},
        {"code": "es"},
    ),
    "default": {
        "fallback": "en",
        "hide_untranslated": False,
    },
}
