from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from rest_framework_simplejwt.views import TokenRefreshView
from rest_framework import permissions
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from communities.api import CommunityViewSet
from clubs.api import ClubViewSet
from category.api import CategoryViewSet
from products.api import ProductViewSet
from accounts.api import UserViewSet, CustomTokenObtainPairView, RegisterView

schema_view = get_schema_view(
   openapi.Info(
      title="Asala API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

router = DefaultRouter()
router.register(r'users', UserViewSet, basename='user')
router.register(r'communities', CommunityViewSet, basename='community')
router.register(r'clubs', ClubViewSet, basename='club')
router.register(r'categories', CategoryViewSet, basename='category')
router.register(r'products', ProductViewSet, basename='product')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('api/auth/login/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/auth/register/', RegisterView.as_view(), name='register'),
    path('api/auth/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
   path('api/search/', include('search.urls')),
   path('api/recommendations/', include('recommendations.urls')),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
