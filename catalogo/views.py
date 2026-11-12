from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Planta
from .forms import PlantaForm


# ---- Vista Basada en Función (FBV) ----
def home(request):
    """Página de inicio. Pasa contexto a la plantilla con render()."""
    total = Planta.objects.count()
    disponibles = Planta.objects.filter(disponible=True).count()
    contexto = {
        "titulo": "Vivero Raíces Verdes",
        "total": total,
        "disponibles": disponibles,
        "destacadas": Planta.objects.filter(disponible=True)[:3],
    }
    return render(request, "catalogo/home.html", contexto)


# ---- Vista Basada en Clase (CBV): listar ----
class PlantaListView(ListView):
    """Lista todas las plantas usando el ListView genérico de Django."""

    model = Planta
    template_name = "catalogo/catalogo.html"
    context_object_name = "plantas"

    def get_context_data(self, **kwargs):
        contexto = super().get_context_data(**kwargs)
        contexto["titulo"] = "Catálogo de plantas"
        return contexto


# ---- CRUD desde la propia interfaz ----
class PlantaCreateView(CreateView):
    """Crea una nueva planta desde un formulario en la web."""
    model = Planta
    form_class = PlantaForm
    template_name = "catalogo/planta_form.html"
    success_url = reverse_lazy("catalogo:lista")

    def get_context_data(self, **kwargs):
        contexto = super().get_context_data(**kwargs)
        contexto["titulo"] = "Agregar planta"
        return contexto


class PlantaUpdateView(UpdateView):
    """Edita una planta existente."""
    model = Planta
    form_class = PlantaForm
    template_name = "catalogo/planta_form.html"
    success_url = reverse_lazy("catalogo:lista")

    def get_context_data(self, **kwargs):
        contexto = super().get_context_data(**kwargs)
        contexto["titulo"] = "Editar planta"
        return contexto


class PlantaDeleteView(DeleteView):
    """Elimina una planta, con confirmación previa."""
    model = Planta
    template_name = "catalogo/planta_confirm_delete.html"
    success_url = reverse_lazy("catalogo:lista")
