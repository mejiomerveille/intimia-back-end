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
from .models import InfoGrossesse
from django.views import View
from .models import InfoGrossesse
from rest_framework import views,status
from rest_framework.permissions import AllowAny
from rest_framework import generics
from rest_framework.response import Response
from .serializer import *

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = GrossesseSerializer

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


def registerGrossesse(self,request):
    grosse = Grossesse.objects.filter(user_id=request.user.id, is_active=True).first()
    if not grosse:
        if request.method in ( 'POST','OPTIONS'):
            form = GrossesseForm(request.POST)
            if form.is_valid():
                grossesse = form.save(commit=False)
                grossesse.user_id = request.user
                grossesse.save()
                return JsonResponse({'success': True, 'date_accouchement': grossesse.end_date})
            else:
                return JsonResponse({'success': False, 'errors': form.errors})
        else:
            form = GrossesseForm()
        content = {
            'user_id': request.user.id,
            'form': form,
        }
        return JsonResponse({'success':'affichage de la grossesse'})
    return JsonResponse({'success': False, 'message': 'Grossesse déjà enregistrée'})

class RegisterGrossesseView(views.APIView):
    def post(self, request):
        user = User.objects.filter(id=request.user.id).first()
        if user:
            grossesse = Grossesse.objects.filter(user_id=user.id, is_active=True).first()
            if not grossesse:
                form = GrossesseForm(request.data)
                if form.is_valid():
                    grossesse = form.save(commit=False)
                    grossesse.user_id = user
                    grossesse.save()
                    return Response({'success': True, 'date_accouchement': grossesse.end_date}, status=status.HTTP_200_OK)
                else:
                    return Response({'success': False, 'errors': form.errors}, status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response({'success': False, 'message': 'Grossesse déjà enregistrée'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'error': 'Invalid user'}, status=status.HTTP_400_BAD_REQUEST)
        
    
    def put(self, request, grossesse_id):
        grossesse = get_object_or_404(Grossesse, id=grossesse_id, user_id=request.user.id)
        form = GrossesseForm(request.data, instance=grossesse)
        if form.is_valid():
            form.save()  # This updates the existing `grossesse` instance
            return Response({'success': True, 'message': 'Grossesse updated successfully'}, status=status.HTTP_200_OK)
        else:
            return Response({'success': False, 'errors': form.errors}, status=status.HTTP_400_BAD_REQUEST)


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

