"""
ASGI config for intimia_backend project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
"""
import os
from django_nextjs.proxy import NextJSProxyHttpConsumer, NextJSProxyWebsocketConsumer
from django.conf import settings

from channels.routing import ProtocolTypeRouter,URLRouter
from django.urls import re_path, path
from django.core.asgi import get_asgi_application
from django.core.asgi import get_asgi_application

# Initialize Django ASGI application early to ensure the AppRegistry
# is populated before importing code that may import ORM models.
django_asgi_app = get_asgi_application()

application = ProtocolTypeRouter({
    "http": django_asgi_app,
    # Just HTTP for now. (We can add other protocols later.)
})

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'intimia_backend.settings')


application = get_asgi_application()


http_routes = [
    re_path(r"", django_asgi_app),
]

websocket_routers = []

if settings.DEBUG:
    http_routes.insert(0, re_path(r"^(?:_next|__next|next).*", NextJSProxyHttpConsumer.as_asgi()))
    websocket_routers.insert(0, path("_next/webpack-hmr", NextJSProxyWebsocketConsumer.as_asgi()))

application = ProtocolTypeRouter(
    {
        "http": URLRouter(http_routes),
        "websocket": URLRouter(websocket_routers),
    }
)

