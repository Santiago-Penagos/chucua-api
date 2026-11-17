import pytest

from payloads import payload

DOMINIOS = ("escenarios", "educativos", "vias", "catastro")


@pytest.mark.parametrize("dominio", DOMINIOS)
def test_ciclo_crud_http(cliente, dominio):
    creada = cliente.post(f"/api/v1/{dominio}", json=payload(dominio, nombre="Original"))
    assert creada.status_code == 201
    entidad_id = creada.json()["properties"]["id"]

    consultada = cliente.get(f"/api/v1/{dominio}/{entidad_id}")
    assert consultada.status_code == 200
    assert consultada.json()["properties"]["nombre"] == "Original"

    actualizada = cliente.put(
        f"/api/v1/{dominio}/{entidad_id}",
        json=payload(dominio, nombre="Actualizada", sector="II"),
    )
    assert actualizada.status_code == 200
    assert actualizada.json()["properties"]["nombre"] == "Actualizada"
    assert actualizada.json()["properties"]["sector"] == "II"

    eliminada = cliente.delete(f"/api/v1/{dominio}/{entidad_id}")
    assert eliminada.status_code == 204
    assert cliente.get(f"/api/v1/{dominio}/{entidad_id}").status_code == 404
