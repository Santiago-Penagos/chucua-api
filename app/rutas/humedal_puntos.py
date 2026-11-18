from chucua_backend.dominio.humedal_puntos import PuntoHumedal

from ..esquemas.humedal_puntos import HumedalPuntosEntrada
from .recurso import crear_router_nuevo

router = crear_router_nuevo(
    dominio="humedal_puntos",
    etiqueta="Puntos Ecológicos Humedal",
    clase=PuntoHumedal,
    esquema=HumedalPuntosEntrada,
    campos=("zona_humedal", "estado_conservacion", "especie_destacada"),
)
