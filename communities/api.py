from rest_framework import viewsets
from communities.models import Community
from communities.serializers import CommunitySerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
class CommunityViewSet(viewsets.ModelViewSet):
    queryset = Community.objects.all().prefetch_related('members')
    serializer_class = CommunitySerializer
    
    @action(detail=True, methods=['post'], url_path='join')
    def toggle_membership(self, request, pk=None):
        community = self.get_object()
        user = request.user
        if user in community.members.all():
            community.members.remove(user)
            return Response({"message": "Left community successfully"}, status=status.HTTP_204_NO_CONTENT)
        else:
            community.members.add(user)
            return Response({"message": "Joined community successfully"}, status=status.HTTP_200_OK)