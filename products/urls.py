from django.urls import path
from .api import ProductListView, ProductLikeView, ProductPurchaseView

urlpatterns = [
    path('', ProductListView.as_view(), name='product-list'),  # Returns all products
    path('<int:product_id>/like/', ProductLikeView.as_view(), name='product-like'),  # Like/Unlike a product
    path('<int:product_id>/purchase/', ProductPurchaseView.as_view(), name='product-purchase'),  # Purchase a product
]
