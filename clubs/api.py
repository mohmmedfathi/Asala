from rest_framework import viewsets
from clubs.models import Club
from clubs.serializers import ClubSerializer
# from accounts.permissions import IsAdminOrOwner
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
class ClubViewSet(viewsets.ModelViewSet):
    queryset = Club.objects.all().prefetch_related('members')
    serializer_class = ClubSerializer
    # permission_classes = [IsAdminOrOwner]

    @action(detail=True, methods=['post'], url_path='join')
    def toggle_membership(self, request, pk=None):
        club = self.get_object()
        user = request.user
        if user in club.members.all():
            club.members.remove(user)
            return Response({"message": "Left club successfully"}, status=status.HTTP_204_NO_CONTENT)
        else:
            club.members.add(user)
            return Response({"message": "Joined club successfully"}, status=status.HTTP_200_OK)