from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    # path('api-auth/', include('rest_framework.urls')),
    path('', include('Comp.urls')),
    path('', include('REP.urls')),
    path('Clientes/', include('Clientes.urls')),
    path('cats/',include('CatSat.urls')),
    path('api/', include('api_Serializers.urls')),
]
if settings.DEBUG: #DEV only
    urlpatterns += static(settings.STATIC_URL, document_root= settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)