from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/token', TokenObtainPairView.as_view(), name='auth.token_pair'),
    path('api/refresh', TokenRefreshView.as_view(), name='auth.token_refresh'),
    path('api/red-social/', include(('red_social.urls', 'red_social')))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
