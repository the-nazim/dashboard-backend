from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from . models import test_Details

class UserDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model=test_Details
        fields = ['first_name', 'last_name', 'email_address', 'user_address', 'user_password', 'date_joined']
        extra_kwargs = {
            'user_password': {'write_only': True},  # Password should not be exposed
        }
    
    def create(self, validated_data):
        validated_data['user_password'] = make_password(validated_data['user_password'])
        return super().create(validated_data)