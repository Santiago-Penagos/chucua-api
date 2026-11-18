from pydantic import Field

from .base import SolicitudEntidad


class CulturaEntrada(SolicitudEntidad):
    tipo_espacio: str = Field(min_length=1)
    actividad_principal: str = Field(min_length=1)
    direccion: str = Field(min_length=1)
    aforo_aproximado: int = Field(ge=0)
