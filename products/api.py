from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from accounts.permissions import IsAdminOrOwner
from products.models import Product
from products.serializers import ProductSerializer

class ProductViewSet(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated, IsAdminOrOwner]  

    def perform_create(self, serializer):
        """Automatically set the authenticated user as the owner of the product."""
        serializer.save(owner=self.request.user)
        
    def get_queryset(self):
        """Filter products to only show those owned by the authenticated user."""
        user = self.request.user
        if user.is_staff:  
            return Product.objects.all()  
        return Product.objects.filter(owner=user)  
