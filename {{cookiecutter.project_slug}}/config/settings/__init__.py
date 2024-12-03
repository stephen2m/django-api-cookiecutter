import os
from pathlib import Path

# Determine which settings file to use based on environment
environment = os.getenv('DJANGO_ENV', 'local')
settings_module = f'config.settings.{environment}'

__all__ = ['settings_module']