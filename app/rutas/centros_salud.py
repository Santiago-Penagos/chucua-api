from chucua_backend.dominio.salud import CentroSalud

from ..esquemas.centros_salud import CentrosSaludEntrada
from .recurso import crear_router_nuevo

router = crear_router_nuevo(
    dominio="centros_salud",
    etiqueta="Centros de Salud",
    clase=CentroSalud,
    esquema=CentrosSaludEntrada,
    campos=("tipo_centro", "nivel_atencion", "horario", "direccion"),
)
