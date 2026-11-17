from app.dependencias import servicio_escenarios
from app.main import app

from payloads import payload


class ServicioRoto:
    def listar(self, sector=None):
        raise RuntimeError("fallo inesperado")


def test_cuerpo_incompleto_responde_422(cliente):
    datos = payload("escenarios")
    datos.pop("nombre")
    respuesta = cliente.post("/api/v1/escenarios", json=datos)
    assert respuesta.status_code == 422
    assert "detail" in respuesta.json()


def test_sector_invalido_responde_422(cliente):
    respuesta = cliente.post(
        "/api/v1/escenarios", json=payload("escenarios", sector="IV")
    )
    assert respuesta.status_code == 422
    assert "detail" in respuesta.json()


def test_geometria_invalida_responde_422(cliente):
    datos = payload("vias")
    datos["geometry"] = {"type": "Point", "coordinates": [-74.16, 4.62]}
    respuesta = cliente.post("/api/v1/vias", json=datos)
    assert respuesta.status_code == 422
    assert "detail" in respuesta.json()


def test_identificador_inexistente_responde_404(cliente):
    respuesta = cliente.get("/api/v1/escenarios/999")
    assert respuesta.status_code == 404
    assert "no existe" in respuesta.json()["detail"]


def test_error_interno_no_expone_trazas(cliente):
    app.dependency_overrides[servicio_escenarios] = lambda: ServicioRoto()
    respuesta = cliente.get("/api/v1/escenarios")
    assert respuesta.status_code == 500
    assert respuesta.json() == {"detail": "Error interno del servidor"}
    assert "Traceback" not in respuesta.text
