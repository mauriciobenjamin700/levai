from uuid import uuid4


def id_generator():
    """
    A simple function that generates a random UUID.

    Returns:
        str: A string representation of a random UUID.
    """
    return str(uuid4())
