from chucua_backend.dominio.educativo import CentroEducativo
from chucua_backend.dominio.geometria_parser import desde_geojson

from ..dependencias import servicio_educativos
from ..esquemas.educativo import EducativoEntrada
from .fabrica import crear_router_recurso


def _entidad(datos: EducativoEntrada) -> CentroEducativo:
    return CentroEducativo(
        nombre=datos.nombre,
        sector=datos.sector,
        geometria=desde_geojson(datos.geometry),
        nivel_educativo=datos.nivel_educativo,
        naturaleza=datos.naturaleza,
    )


router = crear_router_recurso(
    prefijo="educativos",
    etiqueta="Educativos",
    esquema=EducativoEntrada,
    constructor=_entidad,
    dependencia=servicio_educativos,
)
