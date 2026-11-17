from pydantic import Field

from .base import SolicitudEntidad


class ViaEntrada(SolicitudEntidad):
    tipo_via: str = Field(min_length=1)
    estado: str = Field(min_length=1)
