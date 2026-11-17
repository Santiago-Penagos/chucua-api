import pytest

from payloads import payload

TIPOS = {
    "escenarios": "Point",
    "educativos": "Point",
    "vias": "LineString",
    "catastro": "Polygon",
}


@pytest.mark.parametrize("dominio,tipo", TIPOS.items())
def test_crear_devuelve_feature_geojson(cliente, dominio, tipo):
    respuesta = cliente.post(f"/api/v1/{dominio}", json=payload(dominio))
    assert respuesta.status_code == 201
    cuerpo = respuesta.json()
    assert cuerpo["type"] == "Feature"
    assert cuerpo["geometry"]["type"] == tipo
    propiedades = cuerpo["properties"]
    assert propiedades["id"] == 1
    assert propiedades["nombre"] == "Entidad de prueba"
    assert propiedades["sector"] == "I"


@pytest.mark.parametrize("dominio", TIPOS)
def test_listar_devuelve_feature_collection(cliente, dominio):
    cliente.post(f"/api/v1/{dominio}", json=payload(dominio))
    respuesta = cliente.get(f"/api/v1/{dominio}")
    assert respuesta.status_code == 200
    cuerpo = respuesta.json()
    assert cuerpo["type"] == "FeatureCollection"
    assert len(cuerpo["features"]) == 1
    assert cuerpo["features"][0]["properties"]["sector"] == "I"


@pytest.mark.parametrize("dominio", TIPOS)
def test_atributos_propios_en_properties(cliente, dominio):
    respuesta = cliente.post(f"/api/v1/{dominio}", json=payload(dominio))
    propiedades = respuesta.json()["properties"]
    for clave, valor in payload(dominio).items():
        if clave not in {"nombre", "sector", "geometry"}:
            assert propiedades[clave] == valor
