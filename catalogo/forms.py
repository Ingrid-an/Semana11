from django import forms
from .models import Planta


class PlantaForm(forms.ModelForm):
    """Formulario del modelo Planta para crear y editar desde la interfaz."""

    class Meta:
        model = Planta
        fields = ["nombre", "especie", "tamano_cm", "luz", "precio", "disponible"]
        widgets = {
            "nombre": forms.TextInput(attrs={"placeholder": "Monstera"}),
            "especie": forms.TextInput(attrs={"placeholder": "Monstera deliciosa"}),
            "tamano_cm": forms.NumberInput(attrs={"min": 1}),
            "precio": forms.NumberInput(attrs={"step": "0.10", "min": 0}),
        }
