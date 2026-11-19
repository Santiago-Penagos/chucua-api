from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from seed.ejecutar import sembrar

from .config import NOMBRE, VERSION, origenes_cors
from .errores import registrar_manejadores
from .rutas import (
    catastro,
    centros_salud,
    comercio,
    cultura,
    demografia,
    educativos,
    escenarios,
    humedal_puntos,
    jac,
    salud,
    sectores,
    seguridad,
    servicios_publicos,
    transporte,
    vias,
    zonas_verdes,
)

RUTAS = (
    salud.router,
    sectores.router,
    escenarios.router,
    educativos.router,
    vias.router,
    catastro.router,
    jac.router,
    centros_salud.router,
    seguridad.router,
    humedal_puntos.router,
    transporte.router,
    comercio.router,
    cultura.router,
    servicios_publicos.router,
    zonas_verdes.router,
    demografia.router,
)


@asynccontextmanager
async def _ciclo_vida(_app: FastAPI):
    sembrar(fuente="respaldo")
    yield


def crear_app() -> FastAPI:
    app = FastAPI(title=NOMBRE, version=VERSION, lifespan=_ciclo_vida)
    app.add_middleware(
        CORSMiddleware,
        allow_origins=origenes_cors(),
        allow_methods=["*"],
        allow_headers=["*"],
    )
    for router in RUTAS:
        app.include_router(router)
    registrar_manejadores(app)
    return app


app = crear_app()

