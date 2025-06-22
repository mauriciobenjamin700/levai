"""Models for the user app."""
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """
    Custom user model that extends the default Django user model.

    Attributes:
        id (int) : Unique identifier for the user.
        first_name (str) : First name of the user.
        last_name (str) : Last name of the user.
        username (str) : Unique username for the user.
        email (str) : Email address of the user.
        password (str) : Password for the user account.
        is_active (bool) : Indicates if the user account is active.
        is_staff (bool) : Indicates if the user can access the admin site.
        is_superuser (bool) : Indicates if the user has all permissions without explicitly assigning them
        data_joined (datetime) : Date and time when the user joined.
        last_login (datetime) : Date and time of the user's last login.
    """
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "users"
        verbose_name = "User"
        verbose_name_plural = "Users"
        # ordering = ["-created_at"]
        # unique_together = [["username", "email"]]
        # indexes = [
        #     models.Index(fields=["username"], name="username_idx"),
        #     models.Index(fields=["email"], name="email_idx"),
        # ]
        # permissions = [
        #     ("view_user", "Can view user"),
        #     ("edit_user", "Can edit user"),
        #     ("delete_user", "Can delete user"),
        # ]

    def __str__(self):
        return self.username
    
    def to_dict(self):
        """
        Convert the user instance to a dictionary.

        Returns:
            dict: Dictionary representation of the user instance.
        """
        return {
            "id": self.id if hasattr(self, 'id') else None,
            "username": self.username,
            "email": self.email,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "is_active": self.is_active,
            "is_staff": self.is_staff,
            "is_superuser": self.is_superuser,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
        }