from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('market.urls')),
    path('user/', include('user.urls')),
    path('auth/', include("django.contrib.auth.urls")),
    path('appointment/', include('appointment.urls')),
    path('dashboard/', include("dashboard.urls")),
    path('product/', include("product.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
