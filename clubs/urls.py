from django.urls import path
from .api import ClubListView, ClubJoinView

urlpatterns = [
    path('', ClubListView.as_view(), name='club-list'),
    path('<int:club_id>/join/', ClubJoinView.as_view(), name='club-join'),
]
