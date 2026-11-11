from django.db import models


class Planta(models.Model):
    """Modelo que representa una planta del vivero (mapea a una tabla SQLite)."""

    LUZ_OPCIONES = [
        ("sol", "Pleno sol"),
        ("media", "Media sombra"),
        ("sombra", "Sombra"),
    ]

    nombre = models.CharField("Nombre común", max_length=100)
    especie = models.CharField("Especie", max_length=100)
    tamano_cm = models.PositiveIntegerField("Tamaño (cm)", default=20)
    luz = models.CharField("Requerimiento de luz", max_length=10,
                           choices=LUZ_OPCIONES, default="media")
    precio = models.DecimalField("Precio (S/)", max_digits=8, decimal_places=2)
    disponible = models.BooleanField("Disponible", default=True)
    creado_en = models.DateTimeField("Fecha de registro", auto_now_add=True)

    class Meta:
        verbose_name = "Planta"
        verbose_name_plural = "Plantas"
        ordering = ["nombre"]

    def __str__(self):
        """Representación legible del objeto (se ve en el admin y la consola)."""
        return f"{self.nombre} ({self.especie})"
