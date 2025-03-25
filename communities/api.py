from rest_framework import viewsets
from communities.models import Community
from communities.serializers import CommunitySerializer
from accounts.permissions import IsAdminOrOwner

class CommunityViewSet(viewsets.ModelViewSet):
    queryset = Community.objects.all().prefetch_related('members')
    serializer_class = CommunitySerializer
    permission_classes = [IsAdminOrOwner]