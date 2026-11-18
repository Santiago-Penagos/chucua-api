from pydantic import Field

from .base import SolicitudEntidad


class SeguridadEntrada(SolicitudEntidad):
    tipo_punto: str = Field(min_length=1)
    cuadrante: str = Field(min_length=1)
    telefono_contacto: str = Field(min_length=1)
