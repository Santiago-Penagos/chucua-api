from chucua_backend.dominio.servicios_publicos import PuntoServicioPublico

from ..esquemas.servicios_publicos import ServiciosPublicosEntrada
from .recurso import crear_router_nuevo

router = crear_router_nuevo(
    dominio="servicios_publicos",
    etiqueta="Servicios Públicos",
    clase=PuntoServicioPublico,
    esquema=ServiciosPublicosEntrada,
    campos=("tipo_servicio", "estado_operativo", "ubicacion_referencia"),
)
