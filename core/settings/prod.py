from .base import *

DEBUG = False
ROOT_URLCONF = "core.urls"
ADMINS = [
    ("Amedrufai O", "otuozeahmedrufai@gmail.com"),
]
ALLOWED_HOSTS = env("ALLOWED_HOSTS").split(" ")

DATABASES = {
    "default": {
        "ENGINE": env("POSTGRES_ENGINE"),
        "NAME": env("POSTGRES_DB"),
        "USER": env("POSTGRES_USER"),
        "PASSWORD": env("POSTGRES_PASSWORD"),
        "HOST": env("PG_HOST"),
        "PORT": env("PG_PORT"),
    }
}
