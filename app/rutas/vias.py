from chucua_backend.dominio.geometria_parser import desde_geojson
from chucua_backend.dominio.via import EstadoVia

from ..dependencias import servicio_vias
from ..esquemas.via import ViaEntrada
from .fabrica import crear_router_recurso


def _entidad(datos: ViaEntrada) -> EstadoVia:
    return EstadoVia(
        nombre=datos.nombre,
        sector=datos.sector,
        geometria=desde_geojson(datos.geometry),
        tipo_via=datos.tipo_via,
        estado=datos.estado,
    )


router = crear_router_recurso(
    prefijo="vias",
    etiqueta="Vías",
    esquema=ViaEntrada,
    constructor=_entidad,
    dependencia=servicio_vias,
)
