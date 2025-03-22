from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from communities.models import Community
from .serializers import CommunitySerializer

class CommunityListView(generics.ListAPIView):
    queryset = Community.objects.all()
    serializer_class = CommunitySerializer
    
class CommunityJoinView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, community_id):
        try:
            community = Community.objects.get(id=community_id)
        except Community.DoesNotExist:
            return Response({'error': 'Community not found'}, status=status.HTTP_404_NOT_FOUND)

        user = request.user

        if user.joined_communities.filter(id=community.id).exists():
            user.joined_communities.remove(community)
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            user.joined_communities.add(community)
            return Response({
                'message': 'Joined community',
                'joined_communities': list(user.joined_communities.values('id', 'name'))
            }, status=status.HTTP_200_OK)
