from pathlib import Path
import json
from infrastructure.loaders import (
    cargar_guardias_planta,
    cargar_guardias_ocasionales,
    cargar_locaciones,
    cargar_tiempos_od,
)
from services.grafo.grafo import Grafo
from services.guardias.planta import GuardiaPlanta
from services.guardias.ocasionales import GuardiaOcasional
from services.locaciones.locacion import Locacion
from algorithms.initial_solution import construir_solucion_inicial

BASE_PATH = Path("data/inputs")

def crear_grafo_desde_datos(guardias_planta:list=None, locaciones: list=None, tiempos_od:list=None):
    grafo = Grafo()

    for guardia in guardias_planta:
        grafo.agregar_nodo(guardia)

    for locacion in locaciones:
        grafo.agregar_nodo(locacion)

    for guardia in guardias_planta:
        if guardia.id in tiempos_od.tiempos:
            for loc_id, tiempo in tiempos_od.tiempos[guardia.id].items():
                if loc_id in grafo.nodos:
                    grafo.conectar(guardia, grafo.nodos[loc_id], tiempo)

    return grafo

if __name__ == "__main__":
    # Cargar datos
    datos_planta = cargar_guardias_planta(BASE_PATH / "guardias_planta.json")
    datos_ocasionales = cargar_guardias_ocasionales(BASE_PATH / "guardias_ocasionales.json")
    datos_locaciones = cargar_locaciones(BASE_PATH / "locaciones.json")
    tiempos_od = cargar_tiempos_od(BASE_PATH / "tiempos_od.json")

    # Crear nodos guardias
    guardias_planta = []
    for g in datos_planta:
        guardia = GuardiaPlanta(g.id, g.nombre, g.costo_por_turno, g.horas_max_semana)
        guardias_planta.append(guardia)

    guardias_ocasionales = []
    for g in datos_ocasionales:
        guardia = GuardiaOcasional(g.id, g.nombre, g.costo_por_turno)
        guardias_ocasionales.append(guardia)

    # Crear nodos locaciones
    locaciones = []
    for l in datos_locaciones:
        locacion = Locacion(l.id, l.nombre, l.turnos)
        locaciones.append(locacion)

    grafo = crear_grafo_desde_datos(
        guardias_planta=guardias_planta,
        locaciones=locaciones,
        tiempos_od=tiempos_od
    )

    solucion_inicial = construir_solucion_inicial(
        guardias=guardias_planta + guardias_ocasionales,
        locaciones=locaciones,
        dias=["lunes", "martes", "miércoles", "jueves", "viernes"],
        turnos=["mañana", "tarde", "noche"]
    )
    print(f"Solución inicial construida con {len(solucion_inicial)} asignaciones.")
    
    with open("data/outputs/solucion_inicial.json", "w") as f:
        json.dump([asignacion.model_dump() for asignacion in solucion_inicial], f, indent=4)