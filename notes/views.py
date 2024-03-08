from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json
from .models import Note
from .forms import NoteForm
from django.contrib.auth.decorators import login_required

def create_note(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        title = data.get('title', '')
        content = data.get('content', '')
        image = data.get('image', '')
        user = request.user
        print(user)
        note = Note.objects.create(title=title, content=content, image=image, user=user)
        return JsonResponse({'note_id': note.id})
    return JsonResponse({'error': 'Invalid request method'})
# def create_note(request):
#     if request.method == 'POST':
#         form = NoteForm(request.POST, request.FILES)
#         if form.is_valid():
#             note = form.save(commit=False)
#             note.user = request.user
#             note.save()
#             return JsonResponse({'note_id': note.id})
#     else:
#         form = NoteForm()
#     return JsonResponse({'error': 'Invalid request method'})

def get_notes(request):
    notes = Note.objects.all().values()
    return JsonResponse(list(notes), safe=False)
