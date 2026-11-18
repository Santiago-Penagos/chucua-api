from chucua_backend.dominio.seguridad import PuntoSeguridad

from ..esquemas.seguridad import SeguridadEntrada
from .recurso import crear_router_nuevo

router = crear_router_nuevo(
    dominio="seguridad",
    etiqueta="Seguridad Ciudadana",
    clase=PuntoSeguridad,
    esquema=SeguridadEntrada,
    campos=("tipo_punto", "cuadrante", "telefono_contacto"),
)
