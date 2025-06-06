from typing import List
from models.outputs import Asignacion
from services.guardias.planta import GuardiaPlanta
from services.guardias.ocasionales import GuardiaOcasional
from services.locaciones.locacion import Locacion

def construir_solucion_inicial(guardias: List, locaciones: List[Locacion], dias: List[str], turnos: List[str]) -> List[Asignacion]:
    asignaciones = []

    for dia in dias:
        for loc in locaciones:
            for turno in turnos:
                asignado = False

                for g in guardias:
                    if isinstance(g, GuardiaPlanta):
                        if loc.id in g.vecinos and g.vecinos[loc.id] <= 2.5:
                            if g.puede_asignar_turno(dia, 8) and g.asignar_turno(dia, 8):
                                asignaciones.append(Asignacion(
                                    dia=dia,
                                    turno=turno,
                                    id_guardia=g.id,
                                    nombre_guardia=g.nombre,
                                    tipo_guardia=g.tipo,
                                    id_locacion=loc.id,
                                    nombre_locacion=loc.nombre,
                                    costo_turno=g.costo_por_turno
                                ))
                                asignado = True
                                break

                if not asignado:
                    for g in guardias:
                        if isinstance(g, GuardiaOcasional):
                            if loc.id in g.vecinos and g.vecinos[loc.id] <= 2.5:
                                asignaciones.append(Asignacion(
                                    dia=dia,
                                    turno=turno,
                                    id_guardia=g.id,
                                    nombre_guardia=g.nombre,
                                    tipo_guardia=g.tipo,
                                    id_locacion=loc.id,
                                    nombre_locacion=loc.nombre,
                                    costo_turno=g.costo_por_turno
                                ))
                                asignado = True
                                break

                if not asignado:
                    print(f"Advertencia: No se pudo asignar turno {turno} en día {dia} para locación {loc.id}")

    return asignaciones