from rest_framework import serializers
from grossesse.models import Grossesse
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password
from datetime import datetime
from django.http import JsonResponse
from user_module.models import CustomUser as User


class GrossesseSerializer(serializers.ModelSerializer):
    start_date = serializers.DateField(
        required=True,
        validators=[UniqueValidator(queryset=Grossesse.objects.all())]
    )

    class Meta:
        model = Grossesse
        fields = ['start_date', 'end_date', 'user', 'is_active']
        extra_kwargs = {
            'start_date': {'required': True},
        }

    def validate(self, attrs):
        if attrs['start_date'] > datetime.now().date():
            raise serializers.ValidationError({"start_date": "Cette date n'est pas valide"})

        return attrs

    def create(self, validated_data):
        user = self.context['request'].user
        grosse = Grossesse.objects.filter(user_id=user.id, is_active=True).first()
        if not grosse:
            grossesse = Grossesse.objects.create(
                start_date=validated_data['start_date'],
                user_id=user.id
            )

            grossesse.save()

            return grossesse
        return JsonResponse({'error': 'Invalid credentials'})