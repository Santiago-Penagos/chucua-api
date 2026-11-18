from chucua_backend.dominio.cultura import EspacioCultural

from ..esquemas.cultura import CulturaEntrada
from .recurso import crear_router_nuevo

router = crear_router_nuevo(
    dominio="cultura",
    etiqueta="Centros Culturales y Culto",
    clase=EspacioCultural,
    esquema=CulturaEntrada,
    campos=("tipo_espacio", "actividad_principal", "direccion", "aforo_aproximado"),
)
