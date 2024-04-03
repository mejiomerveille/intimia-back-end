from .forms import AppointmentForm
from grossesse.models import Grossesse
from .envoi import send_mail_for_doctor
from django.http import JsonResponse
from rest_framework.views import APIView
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework import status
from .serializers import MedecinSerializer
from .models import RendezVous as Appointment
from .models import Medecin
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view,permission_classes
from django.http import Http404

def messagedv(statut,message:str|None=None,data:list|None=None):
        rowcount = 0 if data is None else len(data)
        return_object ={
            "statut":statut,
            "message":message,
            "data":data,
            "r":rowcount
        }
        return JsonResponse(return_object)

@api_view(['GET'])
@permission_classes([IsAuthenticated])           
def get(request):
    user_id = request.user.id
    appointment = Appointment.objects.filter(user=user_id).values('id','user__username','doctor__name','doctor__profession', 'date','time') or None 
    if appointment is None:
        return messagedv("error","Vous n'avez pas encore enregistré de rendez vous")
    return messagedv(statut="success",data=list(appointment))


@permission_classes([IsAuthenticated])           
@api_view(['DELETE'])   
def delete(request, pk):
    user_id = request.user.id
    try:
        appointment = Appointment.objects.get(pk=pk)
    except Appointment.DoesNotExist:
        raise Http404

    if appointment.user != appointment.user:
        print(appointment.user)
        print(request.user.id)
        return JsonResponse({"message": "Vous n'êtes pas autorisé à supprimer ce rendez-vous."}, status=403, safe=False)

    appointment.delete()
    return JsonResponse({"message": "Rendez-vous supprimé avec succès."}, safe=False)



class DV(APIView):

    def messageGrossesse(self,statut,message:str|None=None,data:list|None=None):
        rowcount = 0 if data is None else len(data)
        return_object ={
            "statut":statut,
            "message":message,
            "data":data,
            "r":rowcount
        }
        return JsonResponse(return_object)
    
    def post(self,request):
        if request.method == 'POST':
            form = AppointmentForm(request.data)
            if form.is_valid():

                user_id=request.user.pk
                appointment = form.save(commit=False)
                id = request.data.get('grossesse_id')
                appointment.user = request.user  
                appointment.modify_by = request.user  
                appointment.create_by = request.user  
                grossesse = Grossesse.objects.filter(user_id=user_id).first() or None
                if(grossesse is None):
                    return self.messageGrossesse("error","Grossesse inaccesible Contact administrateur")
                appointment.grossesse = grossesse
                print(appointment.user.id)
                print(appointment.grossesse)
                appointment.save()
                # Envoyer un e-mail au médecin
                send_mail_for_doctor(user_name=request.user.username, email=appointment.doctor.email, date=appointment.date.strftime("%d-%m-%y"), rdv_name=appointment.doctor.name, heure=appointment.time)
                data = {
                    'message': "Rendez-vous enregistré avec succès",
                }
                return JsonResponse(data, safe=False)
            else:
                print(form)
        else:
            print(request.user)
            form = AppointmentForm(request.data)
        content = {
            'user_id': request.user.id,
            'form': form,
        }
        return JsonResponse('Une erreur est survenue', status=400, safe=False)
    
    def put(self, request, pk):
        try:
            appointment = Appointment.objects.filter(pk=pk)
        except Appointment.DoesNotExist:
            raise Http404

        # if appointment.user != appointment.user:
        #     return JsonResponse({"message": "Vous n'êtes pas autorisé à modifier ce rendez-vous."}, status=403, safe=False)

        form = AppointmentForm(request.data, instance=appointment)
        if form.is_valid():
            appointment = form.save(commit=False)
            appointment.modify_by = request.user
            appointment.save()
            return JsonResponse("Rendez-vous modifié avec succès.", safe=False)
        else:
            return JsonResponse(form.errors, status=400)
        



class MedecinAPIView(APIView):
    def post(self, request):
        serializer = MedecinSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def get_all_medecins(request):
    medecins = Medecin.objects.all().values()
    return JsonResponse(list(medecins), safe=False)