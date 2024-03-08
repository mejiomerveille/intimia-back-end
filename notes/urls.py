from django.urls import path
from notes.views import get_notes, create_note

urlpatterns = [
    path('get_notes/', get_notes, name='get_notes'),
    path('create/', create_note, name='create_note'),
]