# Vivero Raíces Verdes — App Django (Semana 11)

**Asignatura:** Desarrollo de Aplicaciones Web (IS093A) · Unidad II — Desarrollo Web Fullstack
**Tema:** Django 5.x — patrón MTV (Model-Template-View), ORM, FBV y CBV, plantillas con herencia.
**Autora:** Ingrid Ivette Andrade Egoavil

Aplicación web de un vivero que muestra un catálogo de plantas, construida con
Django siguiendo el patrón **MTV**.

---

## Estructura del proyecto

```
vivero_project/            carpeta del proyecto (configuración)
├── manage.py              utilitario de Django
├── requirements.txt
├── .gitignore             excluye db.sqlite3 y __pycache__
├── seed.py                datos de ejemplo (opcional)
├── vivero_project/
│   ├── settings.py        INSTALLED_APPS incluye 'catalogo'
│   ├── urls.py            include('catalogo.urls')
│   └── ...
└── catalogo/              la app
    ├── models.py          modelo Planta (con __str__)
    ├── views.py           home (FBV) + PlantaListView (CBV)
    ├── urls.py            rutas con name para reversibilidad
    ├── admin.py           registro del modelo en el admin
    ├── migrations/
    └── templates/catalogo/
        ├── base.html      plantilla base con bloques
        ├── home.html      extiende base (página de inicio)
        └── catalogo.html  extiende base (tabla con for/if/filtros)
```

---

## Patrón MTV aplicado

- **Model** (`models.py`): la clase `Planta` mapea a una tabla SQLite mediante el
  ORM. Incluye `__str__` para una representación legible.
- **Template** (`templates/`): `base.html` define bloques (`{% block %}`) y las
  demás plantillas la extienden (`{% extends %}`), usando `{% for %}`, `{% if %}`
  y filtros (`title`, `pluralize`, `get_luz_display`).
- **View** (`views.py`): una **FBV** (`home`) con `render()` y contexto, y una
  **CBV** (`PlantaListView`) basada en `ListView`.

---

## Cómo ejecutar (paso a paso)

Requiere **Python 3.11+**.

```bash
# 1. (Recomendado) crear y activar un entorno virtual
python -m venv venv
venv\Scripts\activate        # Windows
# source venv/bin/activate   # Mac/Linux

# 2. Instalar Django
pip install -r requirements.txt

# 3. Crear la base de datos (migraciones)
python manage.py makemigrations
python manage.py migrate

# 4. (Opcional) poblar datos de ejemplo
python manage.py shell < seed.py

# 5. (Opcional) crear superusuario para el admin
python manage.py createsuperuser

# 6. Arrancar el servidor
python manage.py runserver
```

Abrir en el navegador:
- **Inicio (FBV):** http://localhost:8000/
- **Catálogo (CBV):** http://localhost:8000/catalogo/
- **Admin:** http://localhost:8000/admin/

---

## Rutas (routing)

| URL | Vista | Tipo | name |
|---|---|---|---|
| `/` | `home` | FBV | `catalogo:home` |
| `/catalogo/` | `PlantaListView` | CBV (ListView) | `catalogo:lista` |
| `/admin/` | admin de Django | — | — |

---

## Notas de la rúbrica

- Las URLs usan `name` para **reversibilidad** (`{% url 'catalogo:home' %}`).
- `db.sqlite3` está en `.gitignore` y **no se sube** al repositorio.
- Las credenciales/configuración sensible no se modifican de forma insegura.
- `python manage.py check` no reporta problemas.
