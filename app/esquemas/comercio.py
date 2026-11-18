from pydantic import Field

from .base import SolicitudEntidad


class ComercioEntrada(SolicitudEntidad):
    categoria_comercial: str = Field(min_length=1)
    nombre_establecimiento: str = Field(min_length=1)
    direccion: str = Field(min_length=1)
    horario: str = Field(min_length=1)
