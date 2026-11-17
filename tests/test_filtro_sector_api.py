import pytest

from payloads import payload

DOMINIOS = ("escenarios", "educativos", "vias", "catastro")


@pytest.mark.parametrize("dominio", DOMINIOS)
def test_filtro_por_sector(cliente, dominio):
    cliente.post(f"/api/v1/{dominio}", json=payload(dominio, sector="I"))
    cliente.post(f"/api/v1/{dominio}", json=payload(dominio, sector="II"))

    respuesta = cliente.get(f"/api/v1/{dominio}", params={"sector": "I"})
    assert respuesta.status_code == 200
    sectores = {
        feature["properties"]["sector"] for feature in respuesta.json()["features"]
    }
    assert sectores == {"I"}


@pytest.mark.parametrize("dominio", DOMINIOS)
def test_filtro_sin_coincidencias_devuelve_vacio(cliente, dominio):
    cliente.post(f"/api/v1/{dominio}", json=payload(dominio, sector="I"))
    respuesta = cliente.get(f"/api/v1/{dominio}", params={"sector": "III"})
    assert respuesta.status_code == 200
    assert respuesta.json()["features"] == []


@pytest.mark.parametrize("dominio", DOMINIOS)
def test_filtro_invalido_responde_422(cliente, dominio):
    respuesta = cliente.get(f"/api/v1/{dominio}", params={"sector": "IV"})
    assert respuesta.status_code == 422
    assert "detail" in respuesta.json()
