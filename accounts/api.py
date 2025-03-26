from rest_framework import viewsets
from rest_framework.permissions import  IsAuthenticated,AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView
from accounts.serializers.user import UserSerializer, CustomTokenObtainPairSerializer,RegisterSerializer
from accounts.permissions import IsAdminOrOwner
from rest_framework.views import APIView
from rest_framework.response import Response
from accounts.models import CustomUser


class UserViewSet(viewsets.ModelViewSet):
    """
    - **Admins:** Can list, update, and delete any user.
    - **Users:** Can only retrieve and update their own profile.
    """
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated, IsAdminOrOwner]

    def get_queryset(self):
        return CustomUser.objects.all() if self.request.user.is_staff else CustomUser.objects.filter(id=self.request.user.id)

class RegisterView(APIView):
    """
    Public endpoint for user registration.
    """
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response({'message': 'User registered successfully', 'user': UserSerializer(user).data}, status=201)

        # Convert error lists into single strings
        formatted_errors = {field: errors[0] for field, errors in serializer.errors.items()}
        return Response({'message': formatted_errors}, status=400)

class CustomTokenObtainPairView(TokenObtainPairView):
    """
    Custom login view with formatted error messages.
    """
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)

        if response.status_code != 200:
            formatted_errors = {field: errors[0] for field, errors in response.data.items()}
            return Response({'message': formatted_errors}, status=response.status_code)

        return response

