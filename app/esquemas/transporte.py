from pydantic import Field

from .base import SolicitudEntidad


class TransporteEntrada(SolicitudEntidad):
    codigo_paradero: str = Field(min_length=1)
    rutas_alimentadoras: str = Field(min_length=1)
    direccion: str = Field(min_length=1)
    estado_senalizacion: str = Field(min_length=1)
