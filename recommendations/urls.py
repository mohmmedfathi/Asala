from django.urls import path
from .api import RecommendationsView

urlpatterns = [
    path('', RecommendationsView.as_view(), name='recommendations'),
]
