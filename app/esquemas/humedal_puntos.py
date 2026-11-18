from pydantic import Field

from .base import SolicitudEntidad


class HumedalPuntosEntrada(SolicitudEntidad):
    zona_humedal: str = Field(min_length=1)
    estado_conservacion: str = Field(min_length=1)
    especie_destacada: str = Field(min_length=1)
