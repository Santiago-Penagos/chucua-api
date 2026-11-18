from pydantic import Field

from .base import SolicitudEntidad


class ServiciosPublicosEntrada(SolicitudEntidad):
    tipo_servicio: str = Field(min_length=1)
    estado_operativo: str = Field(min_length=1)
    ubicacion_referencia: str = Field(min_length=1)
