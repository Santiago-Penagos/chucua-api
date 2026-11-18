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
    "jac": {"type": "Point", "coordinates": PUNTO},
    "centros_salud": {"type": "Point", "coordinates": PUNTO},
    "seguridad": {"type": "Point", "coordinates": PUNTO},
    "humedal_puntos": {"type": "Point", "coordinates": PUNTO},
    "transporte": {"type": "Point", "coordinates": PUNTO},
    "comercio": {"type": "Point", "coordinates": PUNTO},
    "cultura": {"type": "Point", "coordinates": PUNTO},
    "servicios_publicos": {"type": "Point", "coordinates": PUNTO},
    "zonas_verdes": {"type": "Point", "coordinates": PUNTO},
    "demografia": {"type": "Point", "coordinates": PUNTO},
}

ATRIBUTOS = {
    "escenarios": {"tipo_escenario": "cancha"},
    "educativos": {"nivel_educativo": "basica", "naturaleza": "publico"},
    "vias": {"tipo_via": "residential", "estado": "regular"},
    "catastro": {"uso_suelo": "residencial", "area_m2": 1200},
    "jac": {
        "presidente_contacto": "Contacto 300 000 0000",
        "direccion": "Calle 38 Sur # 79-12",
        "horario_atencion": "Sábados 9:00 a.m.",
    },
    "centros_salud": {
        "tipo_centro": "centro_salud",
        "nivel_atencion": "I",
        "horario": "Lunes a viernes",
        "direccion": "Calle 38 Sur # 79-50",
    },
    "seguridad": {
        "tipo_punto": "CAI",
        "cuadrante": "Cuadrante 12",
        "telefono_contacto": "123",
    },
    "humedal_puntos": {
        "zona_humedal": "ronda_norte",
        "estado_conservacion": "bueno",
        "especie_destacada": "Tingua",
    },
    "transporte": {
        "codigo_paradero": "SITP-001",
        "rutas_alimentadoras": "7-1, 7-2",
        "direccion": "Calle 38 Sur # 79-30",
        "estado_senalizacion": "buena",
    },
    "comercio": {
        "categoria_comercial": "alimentos",
        "nombre_establecimiento": "Panadería La Espiga",
        "direccion": "Calle 38 Sur # 79-18",
        "horario": "Lunes a domingo",
    },
    "cultura": {
        "tipo_espacio": "casa_cultura",
        "actividad_principal": "Talleres de arte",
        "direccion": "Calle 38 Sur # 79-60",
        "aforo_aproximado": 120,
    },
    "servicios_publicos": {
        "tipo_servicio": "acueducto",
        "estado_operativo": "operativo",
        "ubicacion_referencia": "Junto al humedal",
    },
    "zonas_verdes": {
        "area_aprox_m2": 3200,
        "tipo_vegetacion": "arboles_nativos",
        "estado_mantenimiento": "bueno",
        "direccion": "Calle 38 Sur # 79-70",
    },
    "demografia": {
        "poblacion_estimada": 420,
        "hogares_aprox": 120,
        "grupo_etario_predominante": "adultos",
        "anio_censo": 2024,
    },
}

DOMINIOS = tuple(ATRIBUTOS)


def payload(dominio: str, nombre: str = "Entidad de prueba", sector: str = "I") -> dict:
    return {
        "nombre": nombre,
        "sector": sector,
        "geometry": GEOMETRIAS[dominio],
        **ATRIBUTOS[dominio],
    }
