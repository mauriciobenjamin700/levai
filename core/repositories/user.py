"""Module for managing user-related database operations."""
from django.db.models import Q

from apps.user.models import User
from core.schemas import UserRequest, UserResponse


class UserRepository:
    """
    Repository for managing user-related operations in the database.

    Methods:
        add_user(model: User) -> User:
            Add a new user to the database.
        get_user() -> User | list[User] | None:
            Retrieve a user by ID, username, or email.
        update_user(model: User) -> User:
            Update an existing user in the database.
        delete_user(user_id: str) -> bool:
            Delete a user by ID.
    """

    @staticmethod
    def add_user(model: User) -> User:
        """
        Add a new user to the database.

        Args:
            model (User): The user model instance to be added.

        Returns:
            User: The added user model instance.
        """

        existing_user = User.objects.filter(
            Q(email=model.email) | 
            Q(username=model.username)
        ).first()

        if existing_user:
            raise ValueError("E-mail ou nome de usuário já existe.")
        
        model.full_clean()  # Validate the model before saving

        model.save()

        return model
    
    @staticmethod
    def get_user(
        user_id: str | None = None,
        username: str | None = None,
        email: str | None = None,
        all_results: bool = False
    ) -> User | list[User] | None:
        """
        Retrieve a user by ID, username, or email.

        Args:
            user_id (str, optional): The ID of the user to retrieve.
            username (str, optional): The username of the user to retrieve.
            email (str, optional): The email of the user to retrieve.

        Returns:
            User | list[User] | None: The user model instance if found, a list of users if multiple are found,
            or None if no user is found.
        """

        if user_id:
            filters = Q(id=user_id)

        elif username:
            filters = Q(username=username)

        elif email:
            filters = Q(email=email)

        else:
            filters = Q()

        users = User.objects.filter(filters)

        if not users.exists():
            return None
        
        if not all_results:
            return users.first()
        
        return users.all()
    

    @staticmethod
    def update_user(model: User) -> User:
        """
        Update an existing user in the database.

        Args:
            model (User): The user model instance to be updated.

        Returns:
            User: The updated user model instance.
        """

        model.full_clean()

        model.save()

        return model
    
    @staticmethod
    def delete_user(user_id: str) -> bool:
        """
        Delete a user by ID.

        Args:
            user_id (str): The ID of the user to be deleted.

        Returns:
            bool: True if the user was deleted successfully, False otherwise.
        """

        user = User.objects.filter(id=user_id).first()

        if not user:
            return False
        
        user.delete()

        return True
    

    @staticmethod
    def map_request_to_model(request: UserRequest) -> User:
        """
        Map a UserRequest schema to a User instance.

        Args:
            request (UserRequest): The user request schema to be mapped.

        Returns:
            User: The mapped user model instance.
        """

        model = User(
            username=request.name,
            email=request.email,
            password=request.password
        )

        model.set_password(request.password)  # Hash the password

        return model


    @staticmethod
    def map_model_to_response(model: User) -> UserResponse:
        """
        Map a User instance to a UserResponse schema.

        Args:
            model (User): The user model instance to be mapped.

        Returns:
            UserResponse: The mapped user response schema.
        """

        return UserResponse(
            **model.to_dict()
        )
