from pydantic import Field

from .base import SolicitudEntidad


class JacEntrada(SolicitudEntidad):
    presidente_contacto: str = Field(min_length=1)
    direccion: str = Field(min_length=1)
    horario_atencion: str = Field(min_length=1)
