from rest_framework import viewsets
from rest_framework.permissions import  IsAuthenticated,AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView
from accounts.serializers.user import UserSerializer,RegisterSerializer
from accounts.permissions import IsAdminOrOwner 
from rest_framework.views import APIView
from rest_framework.response import Response
from accounts.models import CustomUser
from communities.serializers import CommunitySerializer
from clubs.serializers import ClubSerializer
from products.serializers import ProductSerializer
from rest_framework.decorators import action

class UserViewSet(viewsets.ModelViewSet):

    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated, IsAdminOrOwner]

    def get_queryset(self):
        return CustomUser.objects.all() if self.request.user.is_staff else CustomUser.objects.filter(id=self.request.user.id)
    
    @action(detail=False, methods=['get', 'patch'], permission_classes=[IsAuthenticated])
    def me(self, request):
        user = request.user
        if request.method == 'PATCH':
            serializer = self.get_serializer(user, data=request.data, partial=True)
            serializer.is_valid(raise_exception=True)
            serializer.save()
        

        context = {'request': request}

        data = UserSerializer(user, context=context).data
        data['joined_communities'] = CommunitySerializer(user.joined_communities.all(), many=True, context=context).data
        data['joined_clubs'] = ClubSerializer(user.joined_clubs.all(), many=True, context=context).data
        data['purchased_products'] = ProductSerializer(user.purchased_products.all(), many=True, context=context).data

        return Response(data)


    def retrieve(self, request, *args, **kwargs):

        instance = self.get_object()
        data = UserSerializer(instance).data 

        data['joined_communities'] = CommunitySerializer(instance.joined_communities.all(), many=True).data
        data['joined_clubs'] = ClubSerializer(instance.joined_clubs.all(), many=True).data
        data['purchased_products'] = ProductSerializer(instance.purchased_products.all(), many=True).data

        return Response(data)

class RegisterView(APIView):

    permission_classes = [AllowAny]

    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response({'message': 'User registered successfully', 'user': UserSerializer(user).data}, status=201)

        formatted_errors = " | ".join([f"{field} {errors[0]}" for field, errors in serializer.errors.items()])
        return Response({'message': formatted_errors}, status=400)


class CustomTokenObtainPairView(TokenObtainPairView):
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)

        if response.status_code != 200:
            formatted_errors = " | ".join([f"{field} {errors[0]}" for field, errors in response.data.items()])
            return Response({'message': formatted_errors}, status=response.status_code)

        user = CustomUser.objects.get(username=request.data.get("username"))
        context = {'request': request}

        user_data = UserSerializer(user, context=context).data
        user_data['joined_communities'] = CommunitySerializer(user.joined_communities.all(), many=True, context=context).data
        user_data['joined_clubs'] = ClubSerializer(user.joined_clubs.all(), many=True, context=context).data
        user_data['purchased_products'] = ProductSerializer(user.purchased_products.all(), many=True, context=context).data

        response.data["user"] = user_data
        return response
