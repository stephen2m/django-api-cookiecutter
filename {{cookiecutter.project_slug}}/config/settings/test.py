from .base import *  # noqa

# Debug settings
DEBUG = False

# Use SQLite for tests
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',
    }
}

# Disable password hashing to speed up tests
PASSWORD_HASHERS = [
    'django.contrib.auth.hashers.MD5PasswordHasher',
]

# Disable logging during tests
LOGGING = {}

# Use console email backend
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'