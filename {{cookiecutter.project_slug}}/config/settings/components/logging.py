import os
from datetime import datetime
from pathlib import Path

# Base logging directory
LOG_DIR = Path("/var/log/django")

# Ensure log directory exists
LOG_DIR.mkdir(parents=True, exist_ok=True)

# Create rotating log files based on the current date
def get_log_filename(prefix):
    """Generate log filename with date for rotation"""
    return str(LOG_DIR / f"{prefix}-{datetime.now().strftime('%Y-%m-%d')}.log")


LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '{levelname} [{asctime}] {module} {process:d} {thread:d} {message}',
            'style': '{',
        },
        'simple': {
            'format': '{levelname} [{asctime}] {message}',
            'style': '{',
        },
        'json': {
            'class': 'pythonjsonlogger.jsonlogger.JsonFormatter',
            'format': '%(timestamp)s %(level)s %(name)s %(message)s',
        },
    },
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse',
        },
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'simple',
        },
        'app_file': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': get_log_filename('app'),
            'maxBytes': 1024 * 1024 * 10,  # 10 MB
            'backupCount': 5,
            'formatter': 'verbose',
        },
        'error_file': {
            'level': 'ERROR',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': get_log_filename('error'),
            'maxBytes': 1024 * 1024 * 10,  # 10 MB
            'backupCount': 5,
            'formatter': 'verbose',
        },
        'json_file': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': get_log_filename('json'),
            'maxBytes': 1024 * 1024 * 10,  # 10 MB
            'backupCount': 5,
            'formatter': 'json',
        },
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console', 'error_file'],
            'level': 'INFO',
            'propagate': False,
        },
        'django.server': {
            'handlers': ['console', 'error_file'],
            'level': 'INFO',
            'propagate': False,
        },
        'django.request': {
            'handlers': ['mail_admins', 'error_file'],
            'level': 'ERROR',
            'propagate': False,
        },
        'django.db.backends': {
            'handlers': ['console', 'error_file'],
            'level': 'INFO',
            'propagate': False,
        },
        'apps': {  # Application logs
            'handlers': ['console', 'app_file', 'json_file'],
            'level': 'DEBUG',
            'propagate': False,
        },
    },
}

# Prometheus monitoring configuration
PROMETHEUS_METRICS = {
    'REGISTRY': None,  # Will be created at startup
    'MULTIPROCESS_MODE': 'all',
    'EXPORT_MIGRATIONS': False,
}