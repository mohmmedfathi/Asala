from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Club
from .serializers import ClubSerializer
from rest_framework.permissions import IsAuthenticated

class ClubListView(generics.ListAPIView):
    queryset = Club.objects.all()
    serializer_class = ClubSerializer


class ClubJoinView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, club_id):
        try:
            club = Club.objects.get(id=club_id)
        except Club.DoesNotExist:
            return Response({'error': 'Club not found'}, status=status.HTTP_404_NOT_FOUND)

        user = request.user

        if user.joined_clubs.filter(id=club.id).exists():
            user.joined_clubs.remove(club)
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            user.joined_clubs.add(club)
            return Response({
                'message': 'Joined club',
                'joined_clubs': list(user.joined_clubs.values('id', 'name'))
            }, status=status.HTTP_200_OK)
