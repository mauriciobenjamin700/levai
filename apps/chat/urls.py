from django.urls import path
from apps.chat.views import chat_view, index_view


urlpatterns = [
    path("", chat_view, name="chat"),
    path("chat/", index_view, name="chat_view"),
]