from pydantic import Field

from .base import SolicitudEntidad


class EducativoEntrada(SolicitudEntidad):
    nivel_educativo: str = Field(min_length=1)
    naturaleza: str = Field(min_length=1)
