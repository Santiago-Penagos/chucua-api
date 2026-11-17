from chucua_backend.dominio.escenario import EscenarioDeportivo
from chucua_backend.dominio.geometria_parser import desde_geojson

from ..dependencias import servicio_escenarios
from ..esquemas.escenario import EscenarioEntrada
from .fabrica import crear_router_recurso


def _entidad(datos: EscenarioEntrada) -> EscenarioDeportivo:
    return EscenarioDeportivo(
        nombre=datos.nombre,
        sector=datos.sector,
        geometria=desde_geojson(datos.geometry),
        tipo_escenario=datos.tipo_escenario,
    )


router = crear_router_recurso(
    prefijo="escenarios",
    etiqueta="Escenarios",
    esquema=EscenarioEntrada,
    constructor=_entidad,
    dependencia=servicio_escenarios,
)
