from django.shortcuts import render, redirect, get_object_or_404
from .forms import AppointmentForm,UploadFileForm
from grossesse.models import Grossesse
from django.contrib.auth.models import User
from django.shortcuts import render
from .envoi import send_mail_for_doctor
from django.http import JsonResponse
from django.shortcuts import render, redirect
from rest_framework.decorators import api_view
from .models import RendezVous as Appointment  
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from django.http import JsonResponse


class DV(APIView):
    # @api_view(['POST'])
    def post(self,request):
        if request.method == 'POST':
            form = AppointmentForm(request.data)
            if form.is_valid():
                appointment = form.save(commit=False)
                id = request.data.get('grossesse_id')
                appointment.user = request.user  
                grossesse = get_object_or_404(Grossesse, id=id)
                appointment.grossesse = grossesse
                print(appointment.user)
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


    # @api_view(['GET'])
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