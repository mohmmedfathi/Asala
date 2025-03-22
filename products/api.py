from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Product
from .serializers import ProductSerializer
from rest_framework.permissions import IsAuthenticated


class ProductListView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductLikeView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, product_id):
        try:
            product = Product.objects.get(pk=product_id)
        except Product.DoesNotExist:
            return Response({'error': 'Product not found'}, status=status.HTTP_404_NOT_FOUND)
        
        user = request.user
        if user in product.likes.all():
            product.likes.remove(user)
            return Response(status=status.HTTP_204_NO_CONTENT)  # ✅ Return 204 when unliking
        else:
            product.likes.add(user)
            return Response({'message': 'Product liked'}, status=status.HTTP_200_OK)  # ✅ Return 200 when liking


class ProductPurchaseView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, product_id):
        try:
            product = Product.objects.get(id=product_id)
        except Product.DoesNotExist:
            return Response({'error': 'Product not found'}, status=status.HTTP_404_NOT_FOUND)

        user = request.user

        if user.purchased_products.filter(id=product.id).exists():
            return Response({'message': 'Product already purchased'}, status=status.HTTP_400_BAD_REQUEST)
        
        user.purchased_products.add(product)
        
        return Response({
            'message': 'Product purchased successfully',
            'purchased_products': list(user.purchased_products.values('id', 'name'))
        }, status=status.HTTP_200_OK)


