from .views import send_notification
from django.urls import path

# websocket_urlpatterns = [
    # path(r'ws/notifications/', NotificationConsumer.as_asgi()),

# ]
urlpatterns=[
    path('', send_notification,name='send_notification'),

]