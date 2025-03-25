from drf_writable_nested.serializers import WritableNestedModelSerializer
from accounts.serializers.user import UserSerializer
from .models import Community

class CommunitySerializer(WritableNestedModelSerializer):
    members = UserSerializer(many=True) 

    class Meta:
        model = Community
        fields = ['id', 'name', 'description', 'image', 'members']