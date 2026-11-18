from pydantic import Field

from .base import SolicitudEntidad


class CentrosSaludEntrada(SolicitudEntidad):
    tipo_centro: str = Field(min_length=1)
    nivel_atencion: str = Field(min_length=1)
    horario: str = Field(min_length=1)
    direccion: str = Field(min_length=1)
