def test_sectores_geojson_devuelve_tres_poligonos(cliente):
    respuesta = cliente.get("/sectores/geojson")
    assert respuesta.status_code == 200
    cuerpo = respuesta.json()
    assert cuerpo["type"] == "FeatureCollection"
    assert [f["properties"]["sector"] for f in cuerpo["features"]] == ["I", "II", "III"]


def test_poligonos_de_sectores_estan_cerrados(cliente):
    cuerpo = cliente.get("/sectores/geojson").json()
    for feature in cuerpo["features"]:
        assert feature["geometry"]["type"] == "Polygon"
        anillo = feature["geometry"]["coordinates"][0]
        assert anillo[0] == anillo[-1]
        assert len(anillo) >= 4
