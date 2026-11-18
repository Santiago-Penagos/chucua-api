import sqlite3

from fastapi import Depends

from chucua_backend.repositorios import (
    RepositorioCentrosSalud,
    RepositorioComercio,
    RepositorioCultura,
    RepositorioDemografia,
    RepositorioHumedalPuntos,
    RepositorioJac,
    RepositorioSeguridad,
    RepositorioServiciosPublicos,
    RepositorioTransporte,
    RepositorioZonasVerdes,
)
from chucua_backend.servicios import (
    ServicioCentrosSalud,
    ServicioComercio,
    ServicioCultura,
    ServicioDemografia,
    ServicioHumedalPuntos,
    ServicioJac,
    ServicioSeguridad,
    ServicioServiciosPublicos,
    ServicioTransporte,
    ServicioZonasVerdes,
)

from .dependencias_base import (
    obtener_conexion,
    repo_catastro,
    repo_educativos,
    repo_escenarios,
    repo_vias,
    servicio_catastro,
    servicio_educativos,
    servicio_escenarios,
    servicio_vias,
)

CLASES = {
    "jac": (RepositorioJac, ServicioJac),
    "centros_salud": (RepositorioCentrosSalud, ServicioCentrosSalud),
    "seguridad": (RepositorioSeguridad, ServicioSeguridad),
    "humedal_puntos": (RepositorioHumedalPuntos, ServicioHumedalPuntos),
    "transporte": (RepositorioTransporte, ServicioTransporte),
    "comercio": (RepositorioComercio, ServicioComercio),
    "cultura": (RepositorioCultura, ServicioCultura),
    "servicios_publicos": (RepositorioServiciosPublicos, ServicioServiciosPublicos),
    "zonas_verdes": (RepositorioZonasVerdes, ServicioZonasVerdes),
    "demografia": (RepositorioDemografia, ServicioDemografia),
}


def _repositorio(clase):
    def dependencia(conexion: sqlite3.Connection = Depends(obtener_conexion)):
        return clase(conexion)

    return dependencia


def _servicio(clase, repositorio):
    def dependencia(repo=Depends(repositorio)):
        return clase(repo)

    return dependencia


REPOSITORIOS = {dominio: _repositorio(clases[0]) for dominio, clases in CLASES.items()}
SERVICIOS = {
    dominio: _servicio(clases[1], REPOSITORIOS[dominio])
    for dominio, clases in CLASES.items()
}

__all__ = [
    "obtener_conexion",
    "repo_escenarios",
    "repo_educativos",
    "repo_vias",
    "repo_catastro",
    "servicio_escenarios",
    "servicio_educativos",
    "servicio_vias",
    "servicio_catastro",
    "REPOSITORIOS",
    "SERVICIOS",
]
