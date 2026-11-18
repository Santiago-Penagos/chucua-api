from chucua_backend.dominio.comercio import ComercioLocal

from ..esquemas.comercio import ComercioEntrada
from .recurso import crear_router_nuevo

router = crear_router_nuevo(
    dominio="comercio",
    etiqueta="Comercio Local",
    clase=ComercioLocal,
    esquema=ComercioEntrada,
    campos=("categoria_comercial", "nombre_establecimiento", "direccion", "horario"),
)
