from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Symptom

@api_view(['GET'])
def get_symptom_advice(request, symptom_id):
    try:
        symptom = Symptom.objects.get(id=symptom_id)
        # Écrire du code pour générer des conseils basés sur le symptôme
        advice = f"Conseils pour le symptôme {symptom.name}"
        return Response({'advice': advice})
    except Symptom.DoesNotExist:
        return Response(status=404)