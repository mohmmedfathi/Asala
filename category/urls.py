from django.urls import path
from .views import CategoryListView, CategoryOnlyListView, CategoryProductsView

urlpatterns = [
    path('', CategoryOnlyListView.as_view(), name='category-list'),  # ✅ Returns categories without products
    path('with-products/', CategoryListView.as_view(), name='category-list-with-products'),  # ✅ Returns categories with products
    path('<int:id>/products/', CategoryProductsView.as_view(), name='category-products'),  # ✅ Returns products for a specific category
]
