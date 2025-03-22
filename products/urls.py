from django.urls import path
from .views import ProductListView, ProductLikeView, ProductPurchaseView

urlpatterns = [
    path('', ProductListView.as_view(), name='product-list'),
    path('<int:product_id>/like/', ProductLikeView.as_view(), name='product-like'),
    path('<int:product_id>/purchase/', ProductPurchaseView.as_view(), name='product-purchase'),
]
