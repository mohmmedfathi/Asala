from rest_framework.views import APIView
from rest_framework.response import Response
from accounts.models import CustomUser
from clubs.models import Club
from products.models import Product
from accounts.serializers.user import UserSerializer
from clubs.serializers import ClubSerializer
from products.serializers import ProductSerializer

class RecommendationsView(APIView):
    def get(self, request):
        users = CustomUser.objects.order_by('?')[:3] 
        clubs = Club.objects.order_by('?')[:3]
        products = Product.objects.order_by('?')[:3]

        return Response({
            'users': UserSerializer(users, many=True).data, 
            'clubs': ClubSerializer(clubs, many=True).data,
            'products': ProductSerializer(products, many=True).data,
        })
