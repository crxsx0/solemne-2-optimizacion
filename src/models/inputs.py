from typing import List, Literal, Dict

from pydantic import BaseModel

from config.config import COSTOS_GUARDIAS, HORAS_MAX_SEMANA, TURNOS

class InputGuardiaPlanta(BaseModel):
    """
    Model representing a plant guardian.
    This model can be extended to include specific fields as needed.
    """
    id: str
    nombre: str
    costo_por_turno: float = COSTOS_GUARDIAS['planta']
    horas_max_semana: int = HORAS_MAX_SEMANA
    tipo: Literal["planta"] = "planta"

class GuardiaOcasional(BaseModel):
    """
    Model representing an occasional guardian.
    This model can be extended to include specific fields as needed.
    """
    id: str
    nombre: str
    costo_por_turno: float = COSTOS_GUARDIAS['ocasional']
    tipo: Literal["ocasional"] = "ocasional"

class InputLocaciones(BaseModel):
    """
    Model for input data related to plant locations.
    This model can be extended to include specific fields as needed.
    """
    id: str
    nombre: str
    demanda_diaria: int
    turnos: List[Literal["mañana", "tarde", "noche"]] = TURNOS

class InputLocacionesGuardiasOD(BaseModel):
    """
    Model for input data related to locations of guardians on duty.
    This model can be extended to include specific fields as needed.
    """
    tiempos: Dict[str, Dict[str, float]]
