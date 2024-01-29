from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True)

    
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'first_name', 'last_name', 'password', 'password2', 'is_active')
        

    def validate(self, data):
        if data['password'] != data['password2']:
            raise serializers.ValidationError({'password':'Passwords do not match.'})
        return data
    
    def create(self, validated_data):
        # delete password2
        validated_data.pop('password2')
        user = User.objects.create_user(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user