import pytest


@pytest.fixture
def context():
    """Provide a default context for the template."""
    return {
        "project_name": "Test Project",
        "project_slug": "test_project",
        "app_name": "api",
        "author_name": "Test Author",
        "email": "test@example.com",
        "description": "A test project",
        "version": "0.1.0",
        "use_redis": "y",
        "use_celery": "n",
    }


def test_project_generation(cookies, context):
    """Test if the template generates a valid project."""
    result = cookies.bake(extra_context=context)

    assert result.exit_code == 0
    assert result.exception is None
    assert result.project_path.name == "test_project"
    assert (result.project_path / "pyproject.toml").exists()
    assert (result.project_path / "manage.py").exists()


def test_optional_features(cookies):
    """Test if optional features (e.g., Redis) are included based on context."""
    result = cookies.bake(
        extra_context={
            "project_name": "Redis Enabled",
            "project_slug": "redis_enabled",
            "use_redis": "y",
            "use_celery": "n",
        }
    )
    pyproject_content = (result.project_path / "pyproject.toml").read_text()
    assert "redis = " in pyproject_content
    assert "celery = " not in pyproject_content
