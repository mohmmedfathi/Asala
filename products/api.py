from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from accounts.permissions import IsAdminOrOwner, IsAdminOrProductBuyer
from products.models import Product
from products.serializers import ProductSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action
class ProductViewSet(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated, IsAdminOrProductBuyer]  
    
    def get_queryset(self):
        # user = self.request.user  

        
        # return Product.objects.filter(buyers=user)
        return Product.objects.all()  

    @action(detail=True, methods=['post'], permission_classes=[IsAuthenticated])
    def purchase(self, request, pk=None):
        user = request.user
        try:
            product = Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            return Response({"detail": "Product not found."}, status=status.HTTP_404_NOT_FOUND)
        
        # Add product to the user's purchased_products
        if product not in user.purchased_products.all():
            user.purchased_products.add(product)
            user.save()
            return Response({"detail": f"You have successfully purchased {product.name}!"}, status=status.HTTP_200_OK)
        else:
            return Response({"detail": "You have already purchased this product."}, status=status.HTTP_400_BAD_REQUEST)