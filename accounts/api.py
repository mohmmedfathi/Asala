from django.contrib.auth import authenticate
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny,IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.generics import RetrieveAPIView

from .models import CustomUser
from .serializers import UserSerializer

class RegisterView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = CustomUser.objects.create_user(
                username=serializer.validated_data['username'],
                email=serializer.validated_data['email'],
                password=request.data.get('password'),
                full_name=serializer.validated_data.get('full_name', ''),
                specialization=serializer.validated_data.get('specialization', '')  # ✅ Added specialization
            )
            return Response({
                'message': 'User registered successfully',
                'user': UserSerializer(user).data
            }, status=201)
        return Response(serializer.errors, status=400)

class LoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)
        if user:
            token = RefreshToken.for_user(user)
            return Response({'access': str(token.access_token), 'refresh': str(token)})
        return Response({'error': 'Invalid credentials'}, status=401)

class UserProfileView(RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user