from django.contrib import admin
from django.urls import path, include
from apps.authentication.views import Login
from django.contrib.auth.views import LogoutView
from django.conf.urls.static import static
from django.conf import settings

from apps.blog.views import Home


urlpatterns = [
    path('', Home.as_view(), name='index'),
    path('login/', Login.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('admin/', admin.site.urls),
    path('blog/', include(('apps.blog.urls', 'blog'))),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
