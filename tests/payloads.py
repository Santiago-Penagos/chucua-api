PUNTO = [-74.1685, 4.6285]
LINEA = [[-74.162, 4.627], [-74.161, 4.6275], [-74.160, 4.628]]
POLIGONO = [
    [-74.169, 4.625],
    [-74.1684, 4.625],
    [-74.1684, 4.6256],
    [-74.169, 4.6256],
    [-74.169, 4.625],
]

GEOMETRIAS = {
    "escenarios": {"type": "Point", "coordinates": PUNTO},
    "educativos": {"type": "Point", "coordinates": PUNTO},
    "vias": {"type": "LineString", "coordinates": LINEA},
    "catastro": {"type": "Polygon", "coordinates": [POLIGONO]},
}

ATRIBUTOS = {
    "escenarios": {"tipo_escenario": "cancha"},
    "educativos": {"nivel_educativo": "basica", "naturaleza": "publico"},
    "vias": {"tipo_via": "residential", "estado": "regular"},
    "catastro": {"uso_suelo": "residencial", "area_m2": 1200},
}


def payload(dominio: str, nombre: str = "Entidad de prueba", sector: str = "I") -> dict:
    return {
        "nombre": nombre,
        "sector": sector,
        "geometry": GEOMETRIAS[dominio],
        **ATRIBUTOS[dominio],
    }
