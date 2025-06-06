from typing import List, Literal

from pydantic import BaseModel

class Asignacion(BaseModel):
    """
    Model representing an assignment of a guardian to a location.
    This model can be extended to include specific fields as needed.
    """
    dia: Literal["lunes", "martes", "miércoles", "jueves", "viernes", "sábado", "domingo"]
    turno: Literal["mañana", "tarde", "noche"]
    id_guardia: str
    nombre_guardia: str
    tipo_guardia: Literal["planta", "ocasional"]
    id_locacion: str
    nombre_locacion: str
    costo_turno: float

class OutputData(BaseModel):
    """
    Base model for output data.
    This model can be extended to include specific fields as needed.
    """
    asignaciones: List[Asignacion]
    costo_total_mensual: float
