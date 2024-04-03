from django.urls import path
from .views import *

urlpatterns = [
    path('ajoute', DV.as_view(), name='addappointment'),
    path('get/', get, name='list-rdv'),
    path('medecins/', get_all_medecins, name='get_all_medecins'),
    path('add_medecins/', MedecinAPIView.as_view(), name='medecin-api'),
    path('update/<int:pk>/', DV.as_view(), name='update_rdv'),
    path('<int:pk>/delete/', delete, name='delete_rdv'),
    # path('edit-appointment/<int:appointment_id>/', edit_appointment, name='edit_appointment'),
    # path('upload/<int:appointment_id>/', upload_file, name='upload_file'),
    # path('delete-appointment/<int:appointment_id>/', delete_appointment, name='delete_appointment'),
]