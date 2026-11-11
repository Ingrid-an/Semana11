"""Configuración de URLs del proyecto vivero_project."""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    # Incluye las rutas de la app catalogo (desacoplamiento con include)
    path("", include("catalogo.urls")),
]
