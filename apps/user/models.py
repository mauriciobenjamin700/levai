"""Models for the user app."""
from django.contrib.auth.models import AbstractUser
from django.db import models
from uuid import uuid4


class User(AbstractUser):
    """
    Custom user model that extends the default Django user model.

    Attributes:
        id (str) : Unique identifier for the user.
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
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
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
        return " ,".join([f"{key}: {value}" for key, value in self.to_dict().items()])
    
    def to_dict(self, exclude: list[str] = [], include: dict = {}) -> dict:
        """
        Convert the user instance to a dictionary.

        Returns:
            dict: Dictionary representation of the user instance.
        """
        data = {
            "id": str(self.id) if hasattr(self, 'id') else None,
            "username": self.username,
            "email": self.email,
            "name": f"{self.first_name} {self.last_name}".strip(),
            "is_active": self.is_active,
            "is_staff": self.is_staff,
            "is_superuser": self.is_superuser,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
        }

        for field in exclude:
            data.pop(field, None)

        data.update(include)

        return data