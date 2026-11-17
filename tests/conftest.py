import sys
from pathlib import Path

import pytest
from fastapi.testclient import TestClient

RAIZ_API = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(RAIZ_API))

from app.dependencias import obtener_conexion  # noqa: E402
from app.main import app  # noqa: E402
from chucua_backend.db.conexion import conectar  # noqa: E402


@pytest.fixture()
def cliente(tmp_path):
    ruta = tmp_path / "api.db"

    def conexion_prueba():
        base = conectar(ruta)
        try:
            yield base
        finally:
            base.close()

    app.dependency_overrides[obtener_conexion] = conexion_prueba
    with TestClient(app, raise_server_exceptions=False) as test_client:
        yield test_client
    app.dependency_overrides.clear()
