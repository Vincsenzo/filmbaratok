from decouple import config
from .base import *

DEBUG = True

SECRET_KEY = config('SECRET_KEY')

ALLOWED_HOSTS = ["*"]

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"


try:
    from .local import *
except ImportError:
    pass
