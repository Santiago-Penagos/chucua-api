from typing import Any, Literal

from pydantic import BaseModel, ConfigDict, Field


class Geometria(BaseModel):
    type: Literal["Point", "LineString", "Polygon"]
    coordinates: Any


class Feature(BaseModel):
    type: Literal["Feature"] = "Feature"
    geometry: Geometria
    properties: dict[str, Any]


class FeatureCollection(BaseModel):
    type: Literal["FeatureCollection"] = "FeatureCollection"
    features: list[Feature]


class SolicitudEntidad(BaseModel):
    model_config = ConfigDict(extra="forbid")

    nombre: str = Field(min_length=1)
    sector: Literal["I", "II", "III"]
    geometry: dict[str, Any]
