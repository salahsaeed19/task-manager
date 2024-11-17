from django.urls import path
from .consumers import TaskNotificationConsumer

websocket_urlpatterns = [
    path('ws/tasks/', TaskNotificationConsumer.as_asgi()),
]
