"""Zone to manage the admin interface for the user app.

Register your models here to make them accessible in the Django admin interface.
"""
from django.contrib import admin
from apps.user.models import User


admin.site.register(User)