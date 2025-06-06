import json
from typing import List
from models.inputs import InputGuardiaPlanta, GuardiaOcasional, InputLocaciones, InputLocacionesGuardiasOD

def cargar_guardias_planta(path: str) -> List[InputGuardiaPlanta]:
    """Carga guardias de planta desde un archivo JSON."""
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)
    return [InputGuardiaPlanta(**item) for item in data]

def cargar_guardias_ocasionales(path: str) -> List[GuardiaOcasional]:
    """Carga guardias ocasionales desde un archivo JSON."""
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)
    return [GuardiaOcasional(**item) for item in data]

def cargar_locaciones(path: str) -> List[InputLocaciones]:
    """Carga locaciones desde un archivo JSON."""
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)
    return [InputLocaciones(**item) for item in data]

def cargar_tiempos_od(path: str) -> InputLocacionesGuardiasOD:
    """Carga matriz de tiempos O-D desde un archivo JSON."""
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)
    return InputLocacionesGuardiasOD(**data)
