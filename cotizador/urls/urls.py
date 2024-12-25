
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('refacciones/', include('refacciones.urls')),
    path('clientes/', include('clientes.urls')),
    path('cotizaciones/', include('cotizaciones.urls')),
]
