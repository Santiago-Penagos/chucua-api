from pydantic import Field

from .base import SolicitudEntidad


class CatastroEntrada(SolicitudEntidad):
    uso_suelo: str = Field(min_length=1)
    area_m2: float = Field(gt=0)
