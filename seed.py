"""
seed.py — Puebla la base de datos con plantas de ejemplo.
Uso:  python manage.py shell < seed.py
(Opcional: solo para no tener que agregar las plantas a mano.)
"""
from catalogo.models import Planta

Planta.objects.all().delete()

datos = [
    ("Monstera", "Monstera deliciosa", 60, "media", 45.00, True),
    ("Suculenta Echeveria", "Echeveria elegans", 12, "sol", 15.00, True),
    ("Helecho", "Nephrolepis exaltata", 40, "sombra", 28.00, True),
    ("Cactus San Pedro", "Echinopsis pachanoi", 35, "sol", 32.00, False),
    ("Lavanda", "Lavandula angustifolia", 30, "sol", 22.50, True),
    ("Pothos", "Epipremnum aureum", 25, "media", 18.00, True),
]
for n, e, t, l, p, d in datos:
    Planta.objects.create(nombre=n, especie=e, tamano_cm=t,
                          luz=l, precio=p, disponible=d)

print(f"Plantas creadas: {Planta.objects.count()}")
