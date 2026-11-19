import os

NOMBRE = "API Chucua de la Vaca"
VERSION = "0.1.0"
ORIGENES_PREDETERMINADOS = (
    "http://localhost:5500,http://127.0.0.1:5500,"
    "http://localhost:8000,http://127.0.0.1:8000,"
    "https://santiago-penagos.github.io"
)


def origenes_cors() -> list[str]:
    valor = os.environ.get("CHUCUA_CORS_ORIGINS", ORIGENES_PREDETERMINADOS)
    return [origen.strip() for origen in valor.split(",") if origen.strip()]
