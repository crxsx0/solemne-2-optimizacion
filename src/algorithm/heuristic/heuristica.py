import random
from typing import List
from models.outputs import Asignacion, OutputData
from ..vecindario import (
    swap_guardias_mismo_turno,
    reemplazar_ocasional_por_planta,
    mover_turno_guardia
)

def calcular_costo_total(asignaciones: List[Asignacion]) -> float:
    return sum(a.costo_turno for a in asignaciones)

def busqueda_local(asignaciones: List[Asignacion], guardias: List, iteraciones: int = 1000) -> OutputData:
    mejor_solucion = asignaciones
    mejor_costo = calcular_costo_total(asignaciones)

    for _ in range(iteraciones):
        vecino = random.choice([
            lambda: swap_guardias_mismo_turno(mejor_solucion.copy()),
            lambda: reemplazar_ocasional_por_planta(mejor_solucion.copy(), guardias),
            lambda: mover_turno_guardia(mejor_solucion.copy())
        ])()

        costo_vecino = calcular_costo_total(vecino)
        if costo_vecino < mejor_costo:
            mejor_solucion = vecino
            mejor_costo = costo_vecino

    return OutputData(
        asignaciones=mejor_solucion,
        costo_total_mensual=mejor_costo
    )
