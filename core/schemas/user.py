from datetime import datetime
from core.schemas.base import BaseSchema


class UserRequest(BaseSchema):
    """
    Schema for user registration requests.

    Attributes:
        name (str): The name of the user.
        email (str): The email address of the user.
        password (str): The password for the user account.
    """

    name: str
    email: str
    password: str



class UserResponse(BaseSchema):
    """
    Schema for user response data.

    Attributes:
        id (str): Unique identifier for the user.
        name (str): The name of the user.
        email (str): The email address of the user.
        is_active (bool): Indicates if the user account is active.
        is_staff (bool): Indicates if the user can access the admin site.
        is_superuser (bool): Indicates if the user has all permissions without explicitly assigning them.
    """

    id: str
    name: str
    email: str
    created_at: datetime
    updated_at: datetime


class UserLogin(BaseSchema):
    """
    Schema for user login requests.

    Attributes:
        email (str): The email address of the user.
        password (str): The password for the user account.
    """

    email: str
    password: str