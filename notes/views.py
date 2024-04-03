from django.http import JsonResponse
import json
from .models import Notes
from .forms import NoteForm
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view,permission_classes

 
def messageGrossesse(statut,message:str|None=None,data:list|None=None):
        rowcount = 0 if data is None else len(data)
        return_object ={
            "statut":statut,
            "message":message,
            "data":data,
            "r":rowcount
        }
        return JsonResponse(return_object)

@api_view(['POST'])
@permission_classes([IsAuthenticated])   
def create_note(request):
    if request.method == 'POST':
        print(request.user)
        form = NoteForm(request.data)
        if form.is_valid():
            note=form.save(commit=False)
            note.user=request.user
            note.save()
            print(note)
            data ={
                    'message':"note enregistree avec succes" 
                }
            return JsonResponse(data)
        else:
             print(form)
    else:
        form = NoteForm()
    return JsonResponse('Une erreur est subvenue')

@api_view(['GET'])
@permission_classes([IsAuthenticated])   
def get_notes(request):
    notes = Notes.objects.all().values()
    return JsonResponse(list(notes), safe=False)
