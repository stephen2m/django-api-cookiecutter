import os
import shutil
from pathlib import Path


def clean_optional_files():
    """Remove files based on user choices."""
    if '{{ cookiecutter.use_docker }}' != 'y':
        os.remove('Dockerfile')
        os.remove('docker-compose.yml')

    if '{{ cookiecutter.use_celery }}' != 'y':
        shutil.rmtree('apps/core/tasks')

    if '{{ cookiecutter.use_async }}' != 'y':
        os.remove('config/asgi.py')


def init_git():
    """Initialize git repository."""
    os.system('git init')
    os.system('git add .')
    os.system('git commit -m "Initial commit from cookiecutter template"')


def create_directories():
    """Create necessary directories."""
    directories = [
        'logs',
        'media',
        'staticfiles',
    ]
    
    for directory in directories:
        Path(directory).mkdir(parents=True, exist_ok=True)


def main():
    clean_optional_files()
    create_directories()
    init_git()
    
    print('\nProject initialization completed!')
    print('\nNext steps:')
    print('1. Create and activate a virtual environment')
    print('2. Install dependencies: poetry install')
    print('3. Configure your .env file')
    print('4. Initialize the database')
    print('5. Run migrations')
    
if __name__ == '__main__':
    main()