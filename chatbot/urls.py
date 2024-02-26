from django.urls import path
from .views import save_conversation

urlpatterns = [
    # Autres chemins d'URL
    path('save-conversation/', save_conversation, name='save_conversation'),
]