from rest_framework.views import APIView
from rest_framework.response import Response
from communities.models import Community
from clubs.models import Club
from products.models import Product
from communities.serializers import CommunitySerializer
from clubs.serializers import ClubSerializer
from products.serializers import ProductSerializer

class RecommendationsView(APIView):
    def get(self, request):
        communities = Community.objects.order_by('?')[:3]
        clubs = Club.objects.order_by('?')[:3]
        products = Product.objects.order_by('?')[:3]

        return Response({
            'communities': CommunitySerializer(communities, many=True).data,
            'clubs': ClubSerializer(clubs, many=True).data,
            'products': ProductSerializer(products, many=True).data,
        })
