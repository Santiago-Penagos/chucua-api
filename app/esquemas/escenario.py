from pydantic import Field

from .base import SolicitudEntidad


class EscenarioEntrada(SolicitudEntidad):
    tipo_escenario: str = Field(min_length=1)
