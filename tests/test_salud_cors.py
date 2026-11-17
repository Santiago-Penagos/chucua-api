def test_salud_sin_base_de_datos(cliente):
    respuesta = cliente.get("/api/v1/salud")
    assert respuesta.status_code == 200
    assert respuesta.json()["estado"] == "ok"


def test_preflight_cors_desde_frontend_local(cliente):
    respuesta = cliente.options(
        "/api/v1/salud",
        headers={
            "Origin": "http://localhost:5500",
            "Access-Control-Request-Method": "GET",
        },
    )
    assert respuesta.status_code == 200
    assert respuesta.headers["access-control-allow-origin"] == "http://localhost:5500"
