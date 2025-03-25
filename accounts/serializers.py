from rest_framework import serializers
from .models import CustomUser
from communities.serializers import CommunitySerializer
from clubs.serializers import ClubSerializer
from products.serializers import ProductSerializer

class UserSerializer(serializers.ModelSerializer):
    joined_communities = CommunitySerializer(many=True, read_only=True)
    joined_clubs = ClubSerializer(many=True, read_only=True)
    purchased_products = ProductSerializer(many=True, read_only=True)

    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'full_name','specialization', 
                  'joined_communities', 'joined_clubs', 'purchased_products']
        

