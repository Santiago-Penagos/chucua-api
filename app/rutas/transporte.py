from chucua_backend.dominio.transporte import ParaderoSitp

from ..esquemas.transporte import TransporteEntrada
from .recurso import crear_router_nuevo

router = crear_router_nuevo(
    dominio="transporte",
    etiqueta="Transporte y Paraderos SITP",
    clase=ParaderoSitp,
    esquema=TransporteEntrada,
    campos=(
        "codigo_paradero",
        "rutas_alimentadoras",
        "direccion",
        "estado_senalizacion",
    ),
)
