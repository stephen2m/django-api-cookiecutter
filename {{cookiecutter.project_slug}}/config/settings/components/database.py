import os

{% if cookiecutter.database == "postgres" %}
DATABASES = {
    'default': dj_database_url.config(
        default='postgres://username:@postgres:5432/postgres',
        conn_max_age=int(os.getenv('DATABASE_CONN_MAX_AGE', 600)),
        conn_health_checks=True
    )
}
{% elif cookiecutter.database == "mysql" %}
DATABASES = {
    'default': dj_database_url.config(
        default='mysql://username:@postgres:3306/mysql',
        conn_max_age=int(os.getenv('DATABASE_CONN_MAX_AGE', 600)),
        conn_health_checks=True
    )
}
{% else %}
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'db.sqlite3',
    }
}
{% endif %}