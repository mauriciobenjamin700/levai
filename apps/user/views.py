"""Views for user authentication."""

from django.shortcuts import render

# Create your views here.


def login_view(request):
    """Render the login page.

    Args:
        request: The HTTP request object.

    Returns:
        HttpResponse: The rendered login page.

    """
    return render(request, "login.html")


def register_view(request):
    """Render the registration page.

    Args:
        request: The HTTP request object.

    Returns:
        HttpResponse: The rendered registration page.

    """
    return render(request, "register.html")
