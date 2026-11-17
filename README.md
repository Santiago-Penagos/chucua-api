# chucua-api

API HTTP en FastAPI que expone el CRUD de los cuatro dominios geográficos del
barrio Chucua de la Vaca como GeoJSON.

## Instalación local

Desde `chucua-api`, con el backend hermano ya instalado o no:

```powershell
..\.venv\Scripts\python.exe -m pip install -r requirements.txt
```

`requirements.txt` contiene `-e ../chucua-backend` para desarrollo local. Para
desplegar en **Render**:

1. Publica `chucua-backend` en GitHub.
2. En `requirements.txt`, comenta `-e ../chucua-backend` y descomenta la línea
   `chucua-backend @ git+https://github.com/TU-USUARIO/chucua-backend.git`.
3. Define la variable `CHUCUA_DB_PATH` con una ruta escribible, por ejemplo
   `/opt/render/project/src/chucua.db`.
4. El `Procfile` ya incluye:
   `web: uvicorn app.main:app --host 0.0.0.0 --port $PORT`.

## Arranque

```powershell
..\.venv\Scripts\python.exe -m uvicorn app.main:app --reload
```

- Documentación interactiva: http://localhost:8000/docs
- Salud: http://localhost:8000/api/v1/salud

## Variables de entorno

| Variable            | Uso                                     | Valor por defecto                     |
| ------------------- | --------------------------------------- | ------------------------------------- |
| `CHUCUA_DB_PATH`    | Ruta del archivo SQLite                 | `chucua-backend/chucua.db`            |
| `CHUCUA_CORS_ORIGINS` | Orígenes permitidos, separados por coma | localhost:5500/8000 y 127.0.0.1       |

## Rutas

Todas las rutas de recurso aceptan el filtro `?sector=I|II|III` en el listado.

| Método | Ruta                        | Respuesta                  |
| ------ | --------------------------- | -------------------------- |
| GET    | `/api/v1/salud`             | `{"estado": "ok", ...}`    |
| GET    | `/api/v1/{dominio}`         | `FeatureCollection`        |
| GET    | `/api/v1/{dominio}/{id}`    | `Feature`                  |
| POST   | `/api/v1/{dominio}`         | `Feature` (201)            |
| PUT    | `/api/v1/{dominio}/{id}`    | `Feature`                  |
| DELETE | `/api/v1/{dominio}/{id}`    | Sin cuerpo (204)           |

`{dominio}` ∈ `escenarios`, `educativos`, `vias`, `catastro`.

## Ejemplos

```powershell
# Listar escenarios del sector II
curl.exe "http://localhost:8000/api/v1/escenarios?sector=II"

# Crear un escenario deportivo
curl.exe -X POST "http://localhost:8000/api/v1/escenarios" `
  -H "Content-Type: application/json" `
  -d '{"nombre":"Cancha Nueva","sector":"I","tipo_escenario":"cancha","geometry":{"type":"Point","coordinates":[-74.1685,4.6285]}}'

# Actualizar
curl.exe -X PUT "http://localhost:8000/api/v1/escenarios/1" `
  -H "Content-Type: application/json" `
  -d '{"nombre":"Cancha Renovada","sector":"II","tipo_escenario":"cancha","geometry":{"type":"Point","coordinates":[-74.165,4.628]}}'

# Eliminar
curl.exe -X DELETE "http://localhost:8000/api/v1/escenarios/1"
```

Cuerpo de una vía: `tipo_via`, `estado` y `geometry` `LineString`.
Cuerpo de catastro: `uso_suelo`, `area_m2` y `geometry` `Polygon`.
Cuerpo de centro educativo: `nivel_educativo`, `naturaleza` y `geometry`
`Point`.

## Errores

- `404` con `{"detail": "..."}` si el identificador no existe.
- `422` con `detail` legible si el cuerpo o el sector son inválidos.
- `500` genérico sin trazas ni rutas internas.

## Pruebas

Desde `chucua-api`:

```powershell
..\.venv\Scripts\python.exe -m pytest tests
```

O la suite completa desde `chucua-backend`:

```powershell
..\.venv\Scripts\python.exe -m pytest
```

## Atribución

Datos de origen: *© OpenStreetMap contributors*, licencia **ODbL 1.0**.
