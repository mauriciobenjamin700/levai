from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.dependencies.db import get_session
from app.schemas.user import UserRequest, UserResponse
from app.services.user import UserService

router = APIRouter(prefix="/user", tags=["User"])


@router.post("/")
async def add_user(
    request: UserRequest,
    session: AsyncSession = Depends(get_session),
) -> UserResponse:
    """
    A route to add a user.

    Args:
        request (UserRequest): The user request object.
        session (AsyncSession): The database session.
    Returns:

    """
    service = UserService(session)
    user = await service.add(request)
    return user


@router.get("/")
async def get_users(
    session: AsyncSession = Depends(get_session),
) -> list[UserResponse]:
    """
    A route to get all users.

    Args:
        session (AsyncSession): The database session.
    Returns:
        list[UserResponse]: A list of user response objects.
    """
    service = UserService(session)
    users = await service.get_all()
    return users


@router.get("/{user_id}")
async def get_user(
    user_id: str,
    session: AsyncSession = Depends(get_session),
) -> UserResponse:
    """
    A route to get a user by id.

    Args:
        user_id (str): The id of the user to get.
        session (AsyncSession): The database session.
    Returns:
        UserResponse: The user response object.
    """
    service = UserService(session)
    user = await service.get_by_id(user_id)
    return user


@router.put("/{user_id}")
async def update_user(
    user_id: str,
    request: UserRequest,
    session: AsyncSession = Depends(get_session),
) -> UserResponse:
    """
    A route to update a user by id.

    Args:
        user_id (str): The id of the user to update.
        request (UserRequest): The user request object.
        session (AsyncSession): The database session.
    Returns:
        UserResponse: The user response object.
    """
    service = UserService(session)
    user = await service.update(user_id, request)
    return user


@router.delete("/{user_id}")
async def delete_user(
    user_id: str,
    session: AsyncSession = Depends(get_session),
) -> UserResponse:
    """
    A route to delete a user by id.

    Args:
        user_id (str): The id of the user to delete.
        session (AsyncSession): The database session.
    Returns:
        UserResponse: The user response object.
    """
    service = UserService(session)
    user = await service.delete_by_id(user_id)
    return user
