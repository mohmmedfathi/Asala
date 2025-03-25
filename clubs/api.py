from rest_framework import viewsets
from clubs.models import Club
from clubs.serializers import ClubSerializer
from accounts.permissions import IsAdminOrOwner

class ClubViewSet(viewsets.ModelViewSet):
    queryset = Club.objects.all().prefetch_related('members')
    serializer_class = ClubSerializer
    permission_classes = [IsAdminOrOwner]
