from django.urls import path
from .api import SearchView

urlpatterns = [
    path('', SearchView.as_view(), name='search'),
]
