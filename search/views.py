from rest_framework.response import Response
from rest_framework.views import APIView
from communities.models import Community
from clubs.models import Club
from products.models import Product
from communities.serializers import CommunitySerializer
from clubs.serializers import ClubSerializer
from products.serializers import ProductSerializer

class SearchView(APIView):
    def get(self, request):
        query = request.GET.get('query', '')
        print(query)
        communities = Community.objects.filter(name__icontains=query)
        clubs = Club.objects.filter(name__icontains=query)
        products = Product.objects.filter(name__icontains=query)
        print(communities, clubs, products)
        return Response({
            'communities': CommunitySerializer(communities, many=True).data,
            'clubs': ClubSerializer(clubs, many=True).data,
            'products': ProductSerializer(products, many=True).data
        })
