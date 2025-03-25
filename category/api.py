from rest_framework import viewsets
from category.models import Category
from category.serializers import CategorySerializer
from accounts.permissions import IsAdminOrOwner

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAdminOrOwner]
