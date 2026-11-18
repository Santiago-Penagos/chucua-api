from pydantic import Field

from .base import SolicitudEntidad


class DemografiaEntrada(SolicitudEntidad):
    poblacion_estimada: int = Field(ge=0)
    hogares_aprox: int = Field(ge=0)
    grupo_etario_predominante: str = Field(min_length=1)
    anio_censo: int = Field(ge=1900, le=2100)
