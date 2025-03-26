from rest_framework import serializers
from .models import Club
from accounts.serializers.user import UserSerializer

class ClubSerializer(serializers.ModelSerializer):
    members = UserSerializer(many=True) 
    class Meta:
        model = Club
        fields = ['id', 'name', 'description', 'icon', 'members']

