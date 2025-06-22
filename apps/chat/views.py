from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.

@login_required
def chat_view(request):
    """
    Render the chat view for authenticated users.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: Rendered chat view.
    """
    return render(request, "index.html")


def index_view(request):
    """
    Render the index view for all users.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: Rendered index view.
    """
    return render(request, "index.html")