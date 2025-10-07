from .base import *
import os

DEBUG = True
SECRET_KEY = os.getenv("SECRET_KEY", "dev_secret_key")
ALLOWED_HOSTS = ["*"]

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.getenv("DB_NAME"),
        "USER": os.getenv("DB_USER"),
        "PASSWORD": os.getenv("DB_PASSWORD"),
        "HOST": os.getenv("DB_HOST", "db"),
        "PORT": os.getenv("DB_PORT", 5432),
    }
}

INSTALLED_APPS += [
    "rest_framework",
    "debug_toolbar",
]