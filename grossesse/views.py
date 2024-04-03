from django.http import JsonResponse
from datetime import datetime
from django.shortcuts import render, get_object_or_404,redirect
from user_module.models import CustomUser as User
from .models.models import Grossesse
from .forms import GrossesseForm
from django.http import JsonResponse
from django.shortcuts import render
from .models import InformationGrossesse as InfoGrossesse
from django.views import View
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from .serializer import *
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

class Grossesses(APIView):
    def post(self,request):
            if request.method == 'POST':
                form = GrossesseForm(request.data)
                if form.is_valid():
                    grossesse = form.save(commit=False)
                    grossesse.user = request.user  
                    grossesse.save()
                    data ={
                        ';essage':"grossesse enregistree avec succes", 
                        'date_accouchement': grossesse.end_date
                    }
                    return JsonResponse(data)
                else:
                    print(form)
            else:
                form = GrossesseForm()
            return JsonResponse('Une erreur est subvenue')


class SemaineView(View):
    def get(self, request, num_semaine):
        try:
            info_grossesse = InfoGrossesse.objects.get(semaine__num_semaine=num_semaine)
            semaine_data = info_grossesse.semaine
            return JsonResponse(semaine_data)
        except InfoGrossesse.DoesNotExist:
            return JsonResponse({"error": "Semaine not found"}, status=404)
        

class weekView(View):
    def get(self, request, id_grossesse):
        try:
            info_grossesse = InfoGrossesse.objects.filter(pk=id_grossesse)
            start_date = info_grossesse.start_date 
            current_date = datetime.now().date()
            weeks = (current_date - start_date).days // 7 +1
            return JsonResponse(weeks)
        except InfoGrossesse.DoesNotExist:
            return JsonResponse({"error": "week not found"}, status=404)

@api_view(['GET'])
@permission_classes([IsAuthenticated])  
def get_all_grossesse(request):
    user: User = request.user
    # print(user.id)
    grossesse = Grossesse.objects.filter(user_id=user.id, is_active=True).values('id', 'start_date', 'end_date', 'create_by_id__username', 'user_id__username')
    # print(grossesse)
    if grossesse is not None:
        return messageGrossesse(statut="success",data=list(grossesse))
    return messageGrossesse("error","Grossesse inaccesible Contact administrateur")
    

 
@api_view(['GET'])
@permission_classes([IsAuthenticated]) 
def current_week(request,id_grossesse:None):
    user_id : User= request.user.pk
    pk=id_grossesse 
    g = Grossesse.objects.filter(user_id=user_id ).first()
    grossesse=g.filter(pk=id_grossesse).first() if id_grossesse is not None else g.first()
    print(grossesse)    
    print(request.user)    
    if  grossesse:
        start_date = grossesse.start_date
        current_date = datetime.now().date()
        weeks = (current_date - start_date).days // 7 +1
        return JsonResponse({'week': weeks})
    return JsonResponse({'week': None})

# mejiomerveille@gmail.com
# Modifier une grossesse

def modifier_grossesse(request, grossesse_id):
    grossesse = get_object_or_404(Grossesse, id=grossesse_id, user_id=request.user.id)
    if request.method == 'POST':
        form = GrossesseForm(request.POST, instance=grossesse)
        if form.is_valid():
            grossesse = form.save()
            return redirect('liste_grossesse')
    else:
        form = GrossesseForm(instance=grossesse)
        content = {
        'user_id': request.user.id,
        'form': form,
        'start_date':grossesse.start_date.strftime("%Y-%m-%d")
        }
        return render(request, 'grossesse/modifier_grossesse.html', content,)


 
@api_view(['GET'])
@permission_classes([IsAuthenticated]) 
def principal(request):
    grosse: Grossesse = Grossesse.objects.filter(user_id=request.user.id, is_active=True).first()
    if(grosse):
        if request.method == "GET":
            # recuperer le mois de la grossesse
            user: User = request.user
            grossesse: Grossesse = Grossesse.objects.filter(user_id=user.id, is_active=True).first()
            # month = grossesse.start_date.isoformat().split('-')[2]
            today = datetime.now().date()
            date_diff = (today - grossesse.start_date).days // 7
            # faire les difference entre la date actuelle et la date de depart
            list_weeks = list(range(1, 41))
            # notes=get_notes(request)
            # notes = Note.objects.all()
            # print(notes[0].titre, notes[0].objet)

            return JsonResponse({'start_week': date_diff })
    return JsonResponse('erreur')
    # mervcodemerveille
    # essai
def grossesse_list(request):
    user: User = request.user
    grossesse: Grossesse = Grossesse.objects.filter(user_id=user.id, is_active=True).first()
    if grossesse is not None:
        # grossesse = Grossesse.objects.all()
        return render(request, 'grossesse/list.html', {'grossesse': grossesse})
    return render(request,'chats/404.html')

