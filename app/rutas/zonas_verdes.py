from chucua_backend.dominio.zonas_verdes import ZonaVerde

from ..esquemas.zonas_verdes import ZonasVerdesEntrada
from .recurso import crear_router_nuevo

router = crear_router_nuevo(
    dominio="zonas_verdes",
    etiqueta="Zonas Verdes y Parques",
    clase=ZonaVerde,
    esquema=ZonasVerdesEntrada,
    campos=("area_aprox_m2", "tipo_vegetacion", "estado_mantenimiento", "direccion"),
)
