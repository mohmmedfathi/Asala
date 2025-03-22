from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.response import Response

from .models import Category
from .serializers import CategorySerializer, ProductSerializer

# Get All Categories WITH Products
class CategoryListView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

# Get All Categories WITHOUT Products
class CategoryOnlyListView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def list(self, request, *args, **kwargs):
        categories = self.get_queryset().values('id', 'name', 'description')  #  Exclude products
        return Response(list(categories))

# Get Products of a Specific Category
class CategoryProductsView(RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    lookup_field = "id"  # Fetch category by ID

    def retrieve(self, request, *args, **kwargs):
        category = self.get_object()
        return Response({
            "category": {
                "id": category.id,
                "name": category.name,
                "description": category.description
            },
            "products": ProductSerializer(category.products.all(), many=True).data  # ✅ Fetch products
        })
