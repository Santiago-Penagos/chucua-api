from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .config import NOMBRE, VERSION, origenes_cors
from .errores import registrar_manejadores
from .rutas import catastro, educativos, escenarios, salud, vias


def crear_app() -> FastAPI:
    app = FastAPI(title=NOMBRE, version=VERSION)
    app.add_middleware(
        CORSMiddleware,
        allow_origins=origenes_cors(),
        allow_methods=["*"],
        allow_headers=["*"],
    )
    for router in (
        salud.router,
        escenarios.router,
        educativos.router,
        vias.router,
        catastro.router,
    ):
        app.include_router(router)
    registrar_manejadores(app)
    return app


app = crear_app()
