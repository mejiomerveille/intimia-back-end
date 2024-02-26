from .forms import AppointmentForm
from grossesse.models import Grossesse
from .envoi import send_mail_for_doctor
from django.http import JsonResponse
from .models import RendezVous as Appointment  
from rest_framework.views import APIView
from django.http import JsonResponse
from .models import Medecin
from rest_framework.response import Response
from rest_framework import status
from .serializers import MedecinSerializer

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
                grossesse = Grossesse.objects.filter(user_id=user_id).first() or None
                if(grossesse is None):
                    return self.messageGrossesse("error","Grossesse inaccesible Contact administrateur")
                appointment.grossesse = grossesse
                print(appointment.user.id)
                print(appointment.grossesse)
                appointment.save()
                # Envoyer un e-mail au médecin
                send_mail_for_doctor(user_name=request.user.username, email=appointment.email, date=appointment.date.strftime("%d-%m-%y"), rdv_name=appointment.name, heure=appointment.time)
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


    def get(self,request):
        user = request.user
        appointments = Appointment.objects.all()
        # symptom = Grossesse.objects.get(id)
        # print(symptom)
        events = []
        for appointment in appointments:
            event = {
                'title': appointment.name,
                'time': appointment.time,
                'start': appointment.date.strftime('%Y-%m-%d'),
                'message': "Vous avez rendez-vous le:",
                'profession': appointment.profession,
            }
            events.append(event)

        return Response(events)

# def upload_file(request,appointment_id=None):
#     if request.method == "POST":
#         form_file = UploadFileForm(request.POST, request.FILES)
#         if form_file.is_valid():
#             # file = request.FILES["file"]
#             # handle_uploaded_file(file)
#             rdv = Appointment.objects.get(id=appointment_id) 
#             rdv.file = request.FILES['file']
#             rdv.file_name = request.POST['title']
#             rdv.save()
#             return redirect('list-rdv')
#     return render(request, "rdv/home.html", {"form_file": form_file, "appointment": rdv})


    


        

# def edit_appointment(request, appointment_id):
#     appointment = get_object_or_404(Appointment, id=appointment_id)

#     if request.method == 'POST':
#         appointment_form = AppointmentForm(request.POST, instance=appointment)
#         doctor_form = DoctorForm(request.POST, instance=appointment.doctor)
#         if appointment_form.is_valid() and doctor_form.is_valid():
#             appointment = appointment_form.save()
#             doctor = doctor_form.save()
#             appointment.doctor = doctor
#             appointment.save()
#             return redirect('list-rdv')
#     else:
#         appointment_form = AppointmentForm(instance=appointment)
#         doctor_form = DoctorForm(instance=appointment.doctor)

#     return render(request, 'rdv/edit_appointment.html', {'appointment_form': appointment_form, 'doctor_form': doctor_form})

# def delete_appointment(request, appointment_id):
#     appointment = get_object_or_404(Appointment, id=appointment_id)
#     if request.method == 'POST':
#         appointment.delete()
#         return redirect('list-rdv')

#     return render(request, 'rdv/delete_appointment.html', {'appointment': appointment})