from rest_framework import serializers
from .models import CustomUser
from communities.serializers import CommunitySerializer
from clubs.serializers import ClubSerializer
from products.serializers import ProductSerializer

class UserSerializer(serializers.ModelSerializer):
    joined_communities = serializers.SerializerMethodField()
    joined_clubs = serializers.SerializerMethodField()
    purchased_products = ProductSerializer(many=True, read_only=True)  # this one is fine

    class Meta:
        model = CustomUser
        fields = [
            'id', 'username', 'email', 'full_name', 'specialization',
            'joined_communities', 'joined_clubs', 'purchased_products'
        ]
        read_only_fields = fields

    def get_joined_communities(self, obj):
        
        return CommunitySerializer(obj.joined_communities.all(), many=True).data

    def get_joined_clubs(self, obj):
     
        return ClubSerializer(obj.joined_clubs.all(), many=True).data
