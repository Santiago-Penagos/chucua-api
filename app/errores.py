from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from chucua_backend.errores import EntidadNoEncontrada, ErrorValidacion


def registrar_manejadores(app: FastAPI) -> None:
    @app.exception_handler(EntidadNoEncontrada)
    async def no_encontrada(request: Request, exc: EntidadNoEncontrada):
        return JSONResponse(status_code=404, content={"detail": str(exc)})

    @app.exception_handler(ErrorValidacion)
    async def validacion(request: Request, exc: ErrorValidacion):
        return JSONResponse(status_code=422, content={"detail": str(exc)})

    @app.exception_handler(Exception)
    async def interno(request: Request, exc: Exception):
        return JSONResponse(
            status_code=500, content={"detail": "Error interno del servidor"}
        )
