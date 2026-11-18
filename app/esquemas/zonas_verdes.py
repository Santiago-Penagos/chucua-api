from pydantic import Field

from .base import SolicitudEntidad


class ZonasVerdesEntrada(SolicitudEntidad):
    area_aprox_m2: float = Field(gt=0)
    tipo_vegetacion: str = Field(min_length=1)
    estado_mantenimiento: str = Field(min_length=1)
    direccion: str = Field(min_length=1)
