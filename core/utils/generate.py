from uuid import uuid4

def id_generator():
    """
    Generate a unique identifier for a user.

    Returns:
        str: A unique identifier in the format 'user_<UUID>'.
    """
    return str(uuid4())