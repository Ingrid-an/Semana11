from django.shortcuts import render
from django.views.generic import ListView
from .models import Planta


# ---- Vista Basada en Función (FBV) ----
def home(request):
    """Página de inicio. Pasa contexto a la plantilla con render()."""
    total = Planta.objects.count()
    disponibles = Planta.objects.filter(disponible=True).count()
    contexto = {
        "titulo": "Vivero Raíces Verdes",
        "total": total,
        "disponibles": disponibles,
    }
    return render(request, "catalogo/home.html", contexto)


# ---- Vista Basada en Clase (CBV) ----
class PlantaListView(ListView):
    """Lista todas las plantas usando el ListView genérico de Django."""

    model = Planta
    template_name = "catalogo/catalogo.html"
    context_object_name = "plantas"

    def get_context_data(self, **kwargs):
        """Agrega datos extra al contexto de la plantilla."""
        contexto = super().get_context_data(**kwargs)
        contexto["titulo"] = "Catálogo de plantas"
        return contexto
