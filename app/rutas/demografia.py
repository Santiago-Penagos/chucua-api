from chucua_backend.dominio.demografia import DemografiaSector

from ..esquemas.demografia import DemografiaEntrada
from .recurso import crear_router_nuevo

router = crear_router_nuevo(
    dominio="demografia",
    etiqueta="Población y Demografía",
    clase=DemografiaSector,
    esquema=DemografiaEntrada,
    campos=(
        "poblacion_estimada",
        "hogares_aprox",
        "grupo_etario_predominante",
        "anio_censo",
    ),
)
