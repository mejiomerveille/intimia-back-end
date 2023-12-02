from django.http import JsonResponse
from grossesse.models import Grossesse
from datetime import datetime
from user_module.models import CustomUser as User
from grossesse.models import Grossesse
from .forms import GrossesseForm
from django.http import JsonResponse

# enregistrer la grossesse

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