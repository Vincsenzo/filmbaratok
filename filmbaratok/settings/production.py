from decouple import config
from .base import *

DEBUG = False

SECRET_KEY = config('SECRET_KEY')

ALLOWED_HOSTS = ["filmbaratok.vincsenzo.hu"]

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

try:
    from .local import *
except ImportError:
    pass
