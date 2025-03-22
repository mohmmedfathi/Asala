from django.urls import path
from .views import CommunityListView, CommunityJoinView

urlpatterns = [
    path('', CommunityListView.as_view(), name='community-list'),
    path('<int:community_id>/join/', CommunityJoinView.as_view(), name='community-join'),
]
