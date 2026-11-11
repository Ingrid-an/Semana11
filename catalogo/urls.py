from django.urls import path
from . import views

# Namespace de la app para reversibilidad de URLs
app_name = "catalogo"

urlpatterns = [
    path("", views.home, name="home"),                       # FBV
    path("catalogo/", views.PlantaListView.as_view(), name="lista"),  # CBV
]
