from django.http import JsonResponse
from grossesse.models import Grossesse
from datetime import datetime
from django.shortcuts import render, get_object_or_404,redirect
from user_module.models import CustomUser as User
from grossesse.models import Grossesse
from .forms import GrossesseForm
from .forms import PregnantWomanForm
from .models import WeightWoman
from django.http import JsonResponse
import json
from django.core import serializers
# enregistrer la grossesse

def registerGrossesse(request):

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

# reccuperer la semaine courantge de la grossesse
 
def current_week(request):
    # user: User = request.user
    user_id : User= request.user.id
    grossesse = Grossesse.objects.filter(user_id=1, is_active=True).first()
    print(grossesse)    
    if  grossesse:
        start_date = grossesse.start_date
        current_date = datetime.now().date()
        weeks = (current_date - start_date).days // 7 +1
        
        return JsonResponse({'week': weeks})
    
    return JsonResponse({'week': None})


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

    


def record_data(request):
    if request.method == 'POST':
        form = PregnantWomanForm(request.POST)
        if form.is_valid():
            pregnant_woman = form.save(commit=False)
            pregnant_woman.user = request.user
            pregnant_woman.save()
            return redirect('data_list')
    else:
        form = PregnantWomanForm()
    return render(request, 'grossesse/record_data.html', {'form': form})

def data_list(request):
    data = WeightWoman.objects.filter(user=request.user).order_by('-date_created')
    return render(request, 'grossesse/data_list.html', {'data': data})


def edit_data(request, pk):
    data = get_object_or_404(WeightWoman, pk=pk)
    if request.method == 'POST':
        form = PregnantWomanForm(request.POST, instance=data)
        if form.is_valid():
            form.save()
            return redirect('data_list')
    else:
        form = PregnantWomanForm(instance=data)
    return render(request, 'grossesse/edit_data.html', {'form': form})

def delete_data(request, pk):
    data = get_object_or_404(WeightWoman, pk=pk)
    if request.method == 'POST':
        data.delete()
        return redirect('data_list')
    return render(request, 'grossesse/delete_data.html', {'data': data})






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
    
    
def grossesse_list(request):
    user: User = request.user
    grossesse: Grossesse = Grossesse.objects.filter(user_id=user.id, is_active=True).first()
    if grossesse is not None:
        # grossesse = Grossesse.objects.all()
        return render(request, 'grossesse/list.html', {'grossesse': grossesse})
    return render(request,'chats/404.html')

