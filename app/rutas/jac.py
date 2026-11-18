from chucua_backend.dominio.jac import JuntaAccionComunal

from ..esquemas.jac import JacEntrada
from .recurso import crear_router_nuevo

router = crear_router_nuevo(
    dominio="jac",
    etiqueta="Juntas de Acción Comunal",
    clase=JuntaAccionComunal,
    esquema=JacEntrada,
    campos=("presidente_contacto", "direccion", "horario_atencion"),
)
