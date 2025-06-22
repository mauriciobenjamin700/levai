"""Django app configuration for user authentication."""

from django.apps import AppConfig


class AuthConfig(AppConfig):
    """Configuration for the user authentication app."""

    default_auto_field = "django.db.models.BigAutoField"
    name = "apps.user"
