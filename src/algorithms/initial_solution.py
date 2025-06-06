from typing import List

from models.outputs import Asignacion
from services.guardias.planta import GuardiaPlanta
from services.guardias.ocasionales import GuardiaOcasional
from services.locaciones.locacion import Locacion

def construir_solucion_inicial(
    guardias: List[GuardiaOcasional | GuardiaPlanta],
    locaciones: List[Locacion],
    dias: List[str],
    turnos: List[str],
) -> List[Asignacion]:
    """Construye una solución inicial simple priorizando guardias de planta."""

    asignaciones: List[Asignacion] = []
    guardias_planta = [g for g in guardias if isinstance(g, GuardiaPlanta)]
    guardias_ocasionales = [g for g in guardias if isinstance(g, GuardiaOcasional)]

    for dia in dias:
        for loc in locaciones:
            for turno in turnos:
                for _ in range(loc.demanda_diaria):
                    guardia_seleccionada = None

                    for g in guardias_planta:
                        if loc.id in g.vecinos and g.asignar_turno(8):
                            guardia_seleccionada = g
                            break

                    if guardia_seleccionada is None:
                        for g in guardias_ocasionales:
                            if g.asignar_turno(8):
                                guardia_seleccionada = g
                                break

                    if guardia_seleccionada is None:
                        print(
                            f"No se pudo asignar guardia para {dia} en {loc.nombre} durante el turno {turno}"
                        )
                        continue

                    asignaciones.append(
                        Asignacion(
                            dia=dia,
                            turno=turno,
                            id_guardia=guardia_seleccionada.id,
                            nombre_guardia=guardia_seleccionada.nombre,
                            tipo_guardia=guardia_seleccionada.tipo,
                            id_locacion=loc.id,
                            nombre_locacion=loc.nombre,
                            costo_turno=guardia_seleccionada.costo_por_turno,
                        )
                    )
                    loc.asignar_guardia(dia, turno, guardia_seleccionada)

    return asignaciones
