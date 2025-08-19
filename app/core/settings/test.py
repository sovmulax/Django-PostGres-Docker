from .base import *
import os

# Configuration spécifique pour les tests
DEBUG = False
ENVIRONMENT = 'TEST'

# Utiliser SQLite en mémoire pour les tests (plus rapide et pas besoin de config DB)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',
        'TEST': {
            'NAME': ':memory:',
        },
    }
}

# Désactiver les migrations pour accélérer les tests
class DisableMigrations:
    def __contains__(self, item):
        return True

    def __getitem__(self, item):
        return None

MIGRATION_MODULES = DisableMigrations()

# Désactiver le cache
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
    }
}

# Configuration pour Celery en mode test (synchrone)
CELERY_TASK_ALWAYS_EAGER = True
CELERY_TASK_EAGER_PROPAGATES = True

# Désactiver les logs pendant les tests
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'null': {
            'class': 'logging.NullHandler',
        },
    },
    'root': {
        'handlers': ['null'],
    },
    'loggers': {
        'django': {
            'handlers': ['null'],
            'propagate': False,
        },
    }
}

# Mot de passe simple pour les tests
PASSWORD_HASHERS = [
    'django.contrib.auth.hashers.MD5PasswordHasher',
]

# Variables d'environnement par défaut pour les tests
SECRET_KEY = 'test-secret-key-for-testing-only'
ALLOWED_HOSTS = ['localhost', '127.0.0.1', 'testserver']
ALLOWED_ORIGINS = ['http://localhost', 'http://127.0.0.1']
CSRF_TRUSTED_ORIGINS = ALLOWED_ORIGINS.copy()
