from django.contrib import admin
from .models import Planta


@admin.register(Planta)
class PlantaAdmin(admin.ModelAdmin):
    """Configuración del modelo Planta en el panel de administración."""
    list_display = ("nombre", "especie", "tamano_cm", "luz", "precio", "disponible")
    list_filter = ("luz", "disponible")
    search_fields = ("nombre", "especie")
