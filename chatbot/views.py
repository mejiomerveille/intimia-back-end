from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Conversation

@login_required
def save_conversation(request):
    if request.method == 'POST':
        user = request.user
        user_role = 'user'
        assistant_role = 'assistant'
        
        # Récupérez les données de la requête POST
        user_input = request.POST.get('user_input')
        assistant_response = request.POST.get('assistant_response')
        
        # Enregistrez la conversation dans la base de données
        Conversation.objects.create(user=user,role=user_role, content=user_input)
        Conversation.objects.create(user=user,role=assistant_role, content=assistant_response)
        
        return JsonResponse({'status': 'success'})
    
    return JsonResponse({'status': 'error'})

@login_required
def conversations(request):
    user = request.user
    conversations = Conversation.objects.filter(user=user)
    return JsonResponse(request, 'conversations.html', {'conversations': conversations})