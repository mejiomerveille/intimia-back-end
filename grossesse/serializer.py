from rest_framework import serializers
from grossesse.models import Grossesse

class GrossesseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Grossesse
        fields = ['start_date', 'end_date', 'user_id', 'is_active']
