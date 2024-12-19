from .base import *

DEBUG = False

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-7z%%05px%t!!qe3mrjb=rnn*tu^9ul^1z)&#iqb$y2h17%)yyl"

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = ["filmbaratok.vincsenzo.hu"]

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

try:
    from .local import *
except ImportError:
    pass
