from pathlib import Path
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

BASE_PATH = Path("data/inputs")

def crear_grafo_desde_datos():
    # Cargar datos
    datos_planta = cargar_guardias_planta(BASE_PATH / "guardias_planta.json")
    datos_ocasionales = cargar_guardias_ocasionales(BASE_PATH / "guardias_ocasionales.json")
    datos_locaciones = cargar_locaciones(BASE_PATH / "locaciones.json")
    tiempos_od = cargar_tiempos_od(BASE_PATH / "tiempos_od.json")

    # Instanciar Grafo
    grafo = Grafo()

    # Crear nodos guardias
    guardias = []
    for g in datos_planta:
        guardia = GuardiaPlanta(g.id, g.nombre, g.costo_por_turno, g.horas_max_semana)
        grafo.agregar_nodo(guardia)
        guardias.append(guardia)

    for g in datos_ocasionales:
        guardia = GuardiaOcasional(g.id, g.nombre, g.costo_por_turno)
        grafo.agregar_nodo(guardia)
        guardias.append(guardia)

    # Crear nodos locaciones
    locaciones = []
    for l in datos_locaciones:
        locacion = Locacion(l.id, l.nombre, l.turnos)
        grafo.agregar_nodo(locacion)
        locaciones.append(locacion)

    for guardia in guardias:
        if guardia.id in tiempos_od.tiempos:
            for loc_id, tiempo in tiempos_od.tiempos[guardia.id].items():
                if loc_id in grafo.nodos:
                    grafo.conectar_si_valido(guardia, grafo.nodos[loc_id], tiempo)

    return grafo

if __name__ == "__main__":
    grafo = crear_grafo_desde_datos()
    print(grafo)
    print("Guardias:", len(grafo.obtener_guardias()))
    print("Locaciones:", len(grafo.obtener_locaciones()))