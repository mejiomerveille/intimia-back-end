from django.urls import path
from .views import *

urlpatterns = [
    path('<int:symptom_id>/advice/', get_symptom_advice),

]