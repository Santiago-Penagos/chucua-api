from typing import Callable, Literal

from fastapi import APIRouter, Depends, Query

from ..esquemas.base import Feature, FeatureCollection
from ..geojson import a_coleccion, a_feature

SectorQuery = Literal["I", "II", "III"]


def crear_router_recurso(
    *,
    prefijo: str,
    etiqueta: str,
    esquema,
    constructor: Callable,
    dependencia: Callable,
) -> APIRouter:
    router = APIRouter(prefix=f"/api/v1/{prefijo}", tags=[etiqueta])

    @router.get("", response_model=FeatureCollection)
    def listar(
        sector: SectorQuery | None = Query(default=None),
        servicio=Depends(dependencia),
    ):
        return a_coleccion(servicio.listar(sector))

    @router.get("/{entidad_id}", response_model=Feature)
    def obtener(entidad_id: int, servicio=Depends(dependencia)):
        return a_feature(servicio.obtener(entidad_id))

    @router.post("", response_model=Feature, status_code=201)
    def crear(datos: esquema, servicio=Depends(dependencia)):
        return a_feature(servicio.crear(constructor(datos)))

    @router.put("/{entidad_id}", response_model=Feature)
    def actualizar(entidad_id: int, datos: esquema, servicio=Depends(dependencia)):
        return a_feature(servicio.actualizar(entidad_id, constructor(datos)))

    @router.delete("/{entidad_id}", status_code=204)
    def eliminar(entidad_id: int, servicio=Depends(dependencia)):
        servicio.eliminar(entidad_id)

    return router
