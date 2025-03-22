from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

schema_view = get_schema_view(
   openapi.Info(
      title="Snippets API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
   path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
   path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
   path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
   
    path('admin/', admin.site.urls),
    path('api/auth/', include('accounts.urls')),
    path('api/communities/', include('communities.urls')),
    path('api/clubs/', include('clubs.urls')),
    path('api/products/', include('products.urls')),
    path('api/search/', include('search.urls')),
    path('api/recommendations/', include('recommendations.urls')),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
