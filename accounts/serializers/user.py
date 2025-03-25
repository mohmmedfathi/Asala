from rest_framework import serializers
from accounts.models import CustomUser
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'full_name', 'specialization']
        read_only_fields = ['id', 'email']  # Prevent email changes

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    """Customize JWT token response to include user details."""
    def validate(self, attrs):
        data = super().validate(attrs)
        data['user'] = UserSerializer(self.user).data  # Add user details
        return data

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=8)

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password', 'full_name', 'specialization']

    def create(self, validated_data):
        return CustomUser.objects.create_user(**validated_data)  # Use Django's built-in create_user()