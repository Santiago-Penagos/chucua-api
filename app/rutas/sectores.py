from fastapi import APIRouter

from chucua_backend.geografia import coleccion_sectores

router = APIRouter(tags=["sectores"])


@router.get("/sectores/geojson")
def sectores_geojson() -> dict:
    """Polígonos reales y contiguos de los Sectores I, II y III del barrio."""
    return coleccion_sectores()
