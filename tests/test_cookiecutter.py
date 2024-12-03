import pytest
from itertools import product

# Generate all possible combinations of supported features
def generate_supported_options():
    # Variables with meaningful impact
    pyproject_options = [
        {"use_celery": "y", "use_redis": "y", "database": "postgresql"},
        {"use_celery": "n", "use_redis": "y", "database": "mysql"},
        {"use_celery": "y", "use_redis": "n", "database": "postgresql"},
    ]
    settings_options = [
        {"use_sentry": "y", "auth_method": "jwt"},
        {"use_sentry": "n", "auth_method": "session"},
        {"use_sentry": "n", "auth_method": "token"},
    ]

    # Combine distinct options for meaningful test cases
    return [dict(**pyproj, **settings) for pyproj, settings in product(pyproject_options, settings_options)]


@pytest.fixture
def context():
    """Provide a default context for the template."""
    return {
        "project_name": "Test Project",
        "project_slug": "test_project",
        "app_name": "api",
        "author_name": "Test Author",
        "author_email": "test@example.com",
        "description": "A test project",
        "version": "0.1.0"
    }


@pytest.mark.parametrize("context_override", [
    {"use_celery": "invalid_value", "use_redis": "y", "database": "sqlite"},
    {"use_sentry": "n", "auth_method": None}
])
def test_invalid_context(cookies, context, context_override):
    combined_context = {**context, **context_override}
    result = cookies.bake(extra_context=combined_context)

    assert result.exit_code != 0, f"Invalid context should fail: {combined_context}"
    assert result.exception is not None


@pytest.mark.parametrize("context_override", generate_supported_options())
def test_project_generation(cookies, context, context_override):
    """Test if the template generates a valid project."""
    combined_context = {**context, **context_override}
    result = cookies.bake(extra_context=combined_context)

    assert result.exit_code == 0
    assert result.exception is None
    assert result.project_path.name == context["project_slug"]
    assert result.project_path.is_dir()
    assert (result.project_path / "pyproject.toml").exists(), "pyproject.toml file not found"
    assert (result.project_path / "manage.py").exists(), "manage.py file not found"

    # Validate `pyproject.toml`
    pyproject_path = result.project_path / "pyproject.toml"
    rendered_content = pyproject_path.read_text()

    # Assertions based on context_override
    if combined_context["use_celery"] == "y":
        assert "celery = \"^5.4.0\"" in rendered_content, "Celery configuration missing in pyproject.toml"
    else:
        assert "celery" not in rendered_content , "Celery configuration should not be in pyproject.toml"

    if combined_context["use_redis"] == "y":
        assert "redis = \"^5.2.0\"" in rendered_content, "Redis configuration missing in pyproject.toml"
    else:
        assert "redis" not in rendered_content, "Redis configuration should not be in pyproject.toml"

    if combined_context["database"] == "postgresql":
        assert "psycopg = \"^3.2.3\"" in rendered_content, "Postgres client configuration missing in pyproject.toml"
    elif combined_context["database"] == "mysql":
        assert "mysqlclient = \"^2.2.6\"" in rendered_content, "MySQL configuration missing in pyproject.toml"


    # Validate Django settings
    settings_path = result.project_path / "config" / "settings" / "base.py"
    assert settings_path.exists()
    rendered_settings = settings_path.read_text()

    if combined_context["use_sentry"] == "y":
        assert "SENTRY_DSN" in rendered_settings, "Sentry pypi package configuration missing in the base settings file"
    else:
        assert "SENTRY_DSN" not in rendered_settings, "Sentry pypi configuration should not be in the base settings file"

    if combined_context["auth_method"] == "jwt":
        assert "rest_framework_simplejwt.authentication.JWTAuthentication" in rendered_settings, "Expected Django Rest Framework to use JWT authentication"
    elif combined_context["auth_method"] == "session":
        assert "rest_framework.authentication.SessionAuthentication" in rendered_settings, "Expected Django Rest Framework to use session authentication"
    elif combined_context["auth_method"] == "token":
        assert "rest_framework.authentication.TokenAuthentication" in rendered_settings, "Expected Django Rest Framework to use token authentication"
