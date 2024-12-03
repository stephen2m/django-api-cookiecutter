# {{ cookiecutter.project_name }}

This is a framework for building production-ready Django API-only projects using Django Rest Framework using [Cookiecutter](https://github.com/cookiecutter/cookiecutter).

## Features
- Built with Django Rest Framework
- API-first design
- Easily customizable with cookiecutter

```
project-root/                            # Root template directory
├── cookiecutter.json                    # Template configuration
├── hooks/                               # Generation hooks
│   ├── pre_gen_project.py
│   └── post_gen_project.py
│
├── {{cookiecutter.project_slug}}/       # Generated project directory
│   ├── .env.example                     # Environment variables template
│   ├── .gitignore
│   ├── README.md                        # Project documentation
│   ├── pyproject.toml                   # Dependencies and project metadata
│   ├── Dockerfile
│   ├── docker-compose.yml
│   ├── Makefile                         # Common commands
│   │
│   ├── config/                          # Project configuration
│   │   ├── __init__.py
│   │   ├── urls.py
│   │   ├── wsgi.py
│   │   ├── asgi.py
│   │   │
│   │   └── settings/                    # Layered settings
│   │       ├── __init__.py              # Settings loader
│   │       ├── base.py                  # Base settings
│   │       ├── local.py                 # Development settings
│   │       ├── production.py            # Production settings
│   │       ├── test.py                  # Test settings
│   │       │
│   │       └── components/              # Settings components
│   │           ├── __init__.py
│   │           ├── auth.py
│   │           ├── database.py
│   │           ├── cache.py
│   │           ├── email.py
│   │           └── logging.py
│   │
│   ├── apps/                           # Django applications
│   │   ├── __init__.py
│   │   │
│   │   ├── core/                      # Core functionality
│   │   │   ├── __init__.py
│   │   │   ├── apps.py
│   │   │   ├── exceptions.py
│   │   │   ├── mixins.py
│   │   │   ├── permissions.py
│   │   │   │
│   │   │   ├── models/               # Base models
│   │   │   │   ├── __init__.py
│   │   │   │   └── base.py
│   │   │   │
│   │   │   ├── utils/               # Utility functions
│   │   │   │   ├── __init__.py
│   │   │   │   └── helpers.py
│   │   │   │
│   │   │   └── middleware/          # Custom middleware
│   │   │       ├── __init__.py
│   │   │
│   │   └── api/                     # Main API application
│   │       ├── __init__.py
│   │       ├── apps.py
│   │       ├── urls.py
│   │       │
│   │       ├── models/              # Database models
│   │       │   ├── __init__.py
│   │       │
│   │       ├── serializers/         # API serializers
│   │       │   ├── __init__.py
│   │       │
│   │       ├── services/            # Business logic
│   │       │   ├── __init__.py
│   │       │
│   │       ├── views/               # API views
│   │       │   ├── __init__.py
│   │       │
│   │       └── tests/               # Tests
│   │           ├── __init__.py
│   │           ├── factories/
│   │           ├── integration/
│   │           └── unit/
│   │
│   ├── tests/                       # Project-level tests
│   │   ├── __init__.py
│   │   └── conftest.py
│   │
│   └── scripts/                     # Utility scripts
│       ├── entrypoint.sh
│       └── start.sh
│
└── tests/                           # Template tests
    └── test_cookiecutter.py
```