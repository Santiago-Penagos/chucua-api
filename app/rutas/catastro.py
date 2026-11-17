from chucua_backend.dominio.catastro import InformacionCatastral
from chucua_backend.dominio.geometria_parser import desde_geojson

from ..dependencias import servicio_catastro
from ..esquemas.catastro import CatastroEntrada
from .fabrica import crear_router_recurso


def _entidad(datos: CatastroEntrada) -> InformacionCatastral:
    return InformacionCatastral(
        nombre=datos.nombre,
        sector=datos.sector,
        geometria=desde_geojson(datos.geometry),
        uso_suelo=datos.uso_suelo,
        area_m2=datos.area_m2,
    )


router = crear_router_recurso(
    prefijo="catastro",
    etiqueta="Catastro",
    esquema=CatastroEntrada,
    constructor=_entidad,
    dependencia=servicio_catastro,
)
