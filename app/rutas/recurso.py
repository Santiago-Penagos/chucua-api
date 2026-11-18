from chucua_backend.dominio.geometria_parser import desde_geojson

from ..dependencias import SERVICIOS
from .fabrica import crear_router_recurso


def crear_router_nuevo(*, dominio: str, etiqueta: str, clase, esquema, campos: tuple):
    """Router CRUD para los dominios de punto declarados por configuración."""

    def construir(datos):
        valores = datos.model_dump()
        atributos = {campo: valores[campo] for campo in campos}
        return clase(
            nombre=valores["nombre"],
            sector=valores["sector"],
            geometria=desde_geojson(valores["geometry"]),
            **atributos,
        )

    return crear_router_recurso(
        prefijo=dominio,
        etiqueta=etiqueta,
        esquema=esquema,
        constructor=construir,
        dependencia=SERVICIOS[dominio],
    )
