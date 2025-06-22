"""User service module."""
from django.contrib.auth import authenticate, login, logout
from django.http import HttpRequest

from core.repositories import UserRepository
from core.schemas import UserRequest, UserResponse
from core.schemas.user import UserLogin


class UserService:
    """
    Service for managing user-related operations.

    Methods:
        add_user(model: UserRequest) -> UserResponse:
            Add a new user to the database.
        get_user(user_id: str | None = None, username: str | None = None, email: str | None = None, all_results: bool = False) -> UserResponse | list[UserResponse] | None:
            Retrieve a user by ID, username, or email.
        update_user(model: UserRequest) -> UserResponse:
            Update an existing user in the database.
        delete_user(user_id: str) -> bool:
            Delete a user by ID.
    """

    @staticmethod
    def add_user(request: UserRequest) -> UserResponse:
        """
        Method to add a new user to the database.

        Args:
            request (UserRequest): The user request model containing user data.

        Returns:
            UserResponse: The user response model containing the added user data.
        """

        model = UserRepository.map_request_to_model(request)

        model = UserRepository.add_user(model)

        response = UserRepository.map_model_to_response(model)

        return response
    

    @staticmethod
    def get_user_by_id(user_id: str) -> UserResponse:
        """
        Method to retrieve a user by ID.

        Args:
            user_id (str): The ID of the user to retrieve.

        Returns:
            UserResponse | None: The user response model containing the user data or None if not found.
        """

        model = UserRepository.get_user(user_id=user_id)

        if model is None:
            
            raise ValueError("Usuário não encontrado.")

        response = UserRepository.map_model_to_response(model)

        return response
    

    @staticmethod
    def get_user_by_email(email: str) -> UserResponse:
        """
        Method to retrieve a user by email.

        Args:
            email (str): The email of the user to retrieve.

        Returns:
            UserResponse | None: The user response model containing the user data or None if not found.
        """

        model = UserRepository.get_user(email=email)

        if model is None:
            
            raise ValueError("Usuário não encontrado.")

        response = UserRepository.map_model_to_response(model)

        return response
    

    def update_user(self, request: UserRequest, user_id: str) -> UserResponse:
        """
        Method to update an existing user in the database.

        Args:
            request (UserRequest): The user request model containing updated user data.

        Returns:
            UserResponse: The user response model containing the updated user data.
        """

        model = UserRepository.get_user(user_id=user_id)

        if model is None:
            raise ValueError("Usuário não encontrado.")

        for key, value in request.to_dict().items():
            if value is not None and hasattr(model, key):
                setattr(model, key, value)

        model = UserRepository.update_user(model)

        response = UserRepository.map_model_to_response(model)

        return response
    

    @staticmethod
    def delete_user(user_id: str) -> bool:
        """
        Method to delete a user by ID.

        Args:
            user_id (str): The ID of the user to delete.

        Returns:
            bool: True if the user was deleted successfully, False otherwise.
        """

        return UserRepository.delete_user(user_id)
    

    @staticmethod
    def login(request: HttpRequest, login_request: UserLogin) -> bool:
        """
        Method to log in a user.

        Args:
            request (UserLogin): The user login request model containing email and password.

        Returns:
            Bool: True if the login was successful, False otherwise.
        """

        user = authenticate(
            request, 
            email=login_request.email, 
            password=login_request.password
        )

        if user:
            login(request, user)
            return True
        
        return False
    
    @staticmethod
    def logout(request: HttpRequest) -> bool:
        """
        Method to log out a user.

        Args:
            request (HttpRequest): The HTTP request object.
        """

        if request.user.is_authenticated:
            logout(request)
            return True
        
        return False