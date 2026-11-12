from django.urls import path
from . import views

# Namespace de la app para reversibilidad de URLs
app_name = "catalogo"

urlpatterns = [
    path("", views.home, name="home"),                                 # FBV
    path("catalogo/", views.PlantaListView.as_view(), name="lista"),   # CBV
    # CRUD desde la interfaz
    path("planta/nueva/", views.PlantaCreateView.as_view(), name="crear"),
    path("planta/<int:pk>/editar/", views.PlantaUpdateView.as_view(), name="editar"),
    path("planta/<int:pk>/eliminar/", views.PlantaDeleteView.as_view(), name="eliminar"),
]
