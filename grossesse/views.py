from django.http import JsonResponse
from rest_framework import views,status
from grossesse.models import Grossesse
from rest_framework.response import Response
from datetime import datetime
from django.shortcuts import render, get_object_or_404,redirect
from user_module.models import CustomUser as User
from grossesse.models import Grossesse
from .forms import GrossesseForm
from django.http import JsonResponse
from django.shortcuts import render
from .models import InformationGrossesse as InfoGrossesse
from django.views import View
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from .serializer import *

class Grossesse(APIView):
    permission_classes = (AllowAny,)
    # serializer_class = GrossesseSerializer
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
            content = {
                'user_id': request.user.id,
                'form': form,
            }
            return JsonResponse('Une erreur est subvenue')


class SemaineView(View):
    def get(self, request, num_semaine):
        try:
            info_grossesse = InfoGrossesse.objects.get(semaine__num_semaine=num_semaine)
            semaine_data = info_grossesse.semaine
            return JsonResponse(semaine_data)
        except InfoGrossesse.DoesNotExist:
            return JsonResponse({"error": "Semaine not found"}, status=404)

def current_week(request, current_week):
    try:
        info_grossesse = InfoGrossesse.objects.get(semaine__num_semaine=current_week)
        semaine_data = info_grossesse.semaine
        return JsonResponse(semaine_data)
    except InfoGrossesse.DoesNotExist:
        return JsonResponse({'message': 'Aucune donnée disponible pour cette semaine'})


# reccuperer la semaine courantge de la grossesse
 
# def current_week(request):
#     # user: User = request.user
#     user_id : User= request.user.id
#     grossesse = Grossesse.objects.filter(user_id=1, is_active=True).first()
#     print(grossesse)    
#     if  grossesse:
#         start_date = grossesse.start_date
#         current_date = datetime.now().date()
#         weeks = (current_date - start_date).days // 7 +1
        
#         return JsonResponse({'week': weeks})
    
#     return JsonResponse({'week': None})


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

            return render(request, 'grossesse/cadre.html',{'n':list_weeks, 'start_week': date_diff })
    return render(request,'app/404.html')
    # mervcodemerveille
    # essai
def grossesse_list(request):
    user: User = request.user
    grossesse: Grossesse = Grossesse.objects.filter(user_id=user.id, is_active=True).first()
    if grossesse is not None:
        # grossesse = Grossesse.objects.all()
        return render(request, 'grossesse/list.html', {'grossesse': grossesse})
    return render(request,'chats/404.html')

