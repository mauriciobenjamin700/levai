from pydantic import Field

from app.core.constants.enums.user import UserRoles
from app.schemas.settings.base import BaseSchema
from app.schemas.settings.validators import (
    validate_created_at,
    validate_email,
    validate_id,
    validate_name,
    validate_password,
    validate_phone,
    validate_updated_at,
)


class UserBase(BaseSchema):
    """
    Base class for user schemas.

    Args:
        name (str): The name of the user.
        phone (str): The phone number of the user.
        email (str): The email address of the user.
    """

    name: str = Field(
        examples=["John Doe"], default=None, validate_default=True
    )
    phone: str = Field(
        examples=["89 91234-5678"], default=None, validate_default=True
    )
    email: str = Field(
        examples=["test@gmail.com"], default=None, validate_default=True
    )

    __name_validator = validate_name
    __phone_validator = validate_phone
    __email_validator = validate_email


class UserRequest(UserBase):
    """
    Class to validate the request body of the user register endpoint.

    Args:
        name (str): The name of the user.
        phone (str): The phone number of the user.
        email (str): The email address of the user.
        password (str): The password of the user.
    """

    password: str = Field(
        examples=["password123"], default=None, validate_default=True
    )

    __password_validator = validate_password


class UserResponse(UserBase):
    """
    Class to contain data about the user.

    Args:
        id (str): The id of the user.
        name (str): The name of the user.
        phone (str): The phone number of the user.
        email (str): The email address of the user.
        role (UserRoles): The role of the user.
        created_at (str): The date when the user was created.
        updated_at (str): The date when the user was updated.
    """

    id: str = Field(
        examples=["1234567890"], default=None, validate_default=True
    )
    role: UserRoles = Field(
        examples=[UserRoles.USER.value], default=None, validate_default=True
    )
    created_at: str = Field(
        examples=["2023-10-01 12:00:00"], default=None, validate_default=True
    )
    updated_at: str = Field(
        examples=["2023-10-01 12:00:00"], default=None, validate_default=True
    )

    __id_validator = validate_id
    __created_at_validator = validate_created_at
    __updated_at_validator = validate_updated_at
