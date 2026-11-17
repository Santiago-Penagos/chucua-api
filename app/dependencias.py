import sqlite3

from fastapi import Depends

from chucua_backend.db.conexion import conectar
from chucua_backend.dominio.catastro import InformacionCatastral
from chucua_backend.dominio.educativo import CentroEducativo
from chucua_backend.dominio.escenario import EscenarioDeportivo
from chucua_backend.dominio.via import EstadoVia
from chucua_backend.repositorios.catastro import RepositorioCatastro
from chucua_backend.repositorios.contrato import IRepositorioCRUD
from chucua_backend.repositorios.educativos import RepositorioEducativos
from chucua_backend.repositorios.escenarios import RepositorioEscenarios
from chucua_backend.repositorios.vias import RepositorioVias
from chucua_backend.servicios.catastro import ServicioCatastro
from chucua_backend.servicios.educativos import ServicioEducativos
from chucua_backend.servicios.escenarios import ServicioEscenarios
from chucua_backend.servicios.vias import ServicioVias


def obtener_conexion():
    conexion = conectar()
    try:
        yield conexion
    finally:
        conexion.close()


def repo_escenarios(
    conexion: sqlite3.Connection = Depends(obtener_conexion),
) -> RepositorioEscenarios:
    return RepositorioEscenarios(conexion)


def repo_educativos(
    conexion: sqlite3.Connection = Depends(obtener_conexion),
) -> RepositorioEducativos:
    return RepositorioEducativos(conexion)


def repo_vias(
    conexion: sqlite3.Connection = Depends(obtener_conexion),
) -> RepositorioVias:
    return RepositorioVias(conexion)


def repo_catastro(
    conexion: sqlite3.Connection = Depends(obtener_conexion),
) -> RepositorioCatastro:
    return RepositorioCatastro(conexion)


def servicio_escenarios(
    repositorio: IRepositorioCRUD[EscenarioDeportivo] = Depends(repo_escenarios),
) -> ServicioEscenarios:
    return ServicioEscenarios(repositorio)


def servicio_educativos(
    repositorio: IRepositorioCRUD[CentroEducativo] = Depends(repo_educativos),
) -> ServicioEducativos:
    return ServicioEducativos(repositorio)


def servicio_vias(
    repositorio: IRepositorioCRUD[EstadoVia] = Depends(repo_vias),
) -> ServicioVias:
    return ServicioVias(repositorio)


def servicio_catastro(
    repositorio: IRepositorioCRUD[InformacionCatastral] = Depends(repo_catastro),
) -> ServicioCatastro:
    return ServicioCatastro(repositorio)
