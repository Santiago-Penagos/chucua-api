from chucua_backend.dominio.entidad import EntidadGeografica


def a_feature(entidad: EntidadGeografica) -> dict:
    return entidad.a_geojson()


def a_coleccion(entidades: list[EntidadGeografica]) -> dict:
    return {
        "type": "FeatureCollection",
        "features": [a_feature(entidad) for entidad in entidades],
    }
