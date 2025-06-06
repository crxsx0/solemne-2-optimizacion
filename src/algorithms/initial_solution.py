from typing import List
from models.outputs import Asignacion
from services.guardias.planta import GuardiaPlanta
from services.guardias.ocasionales import GuardiaOcasional
from services.locaciones.locacion import Locacion

def construir_solucion_inicial(guardias: List[GuardiaOcasional|GuardiaPlanta], locaciones: List[Locacion], dias: List[str], turnos: List[str]) -> List[Asignacion]:
    asignaciones = []

    for dia in dias:
        for loc in locaciones:
            for turno in turnos:
                asignado = False

                for g in guardias:
                    if g.asignar_turno(8):
                        asignacion = Asignacion(
                            dia=dia,
                            turno=turno,
                            id_guardia=g.id,
                            nombre_guardia=g.nombre,
                            tipo_guardia=g.tipo,
                            id_locacion=loc.id,
                            nombre_locacion=loc.nombre,
                            costo_turno=g.costo_por_turno
                        )
                        asignaciones.append(asignacion)
                        asignado = True
                        break
                if not asignado:
                    # Si no se pudo asignar un guardia, se puede manejar el caso aquí
                    print(f"No se pudo asignar guardia para {dia} en {loc.nombre} durante el turno {turno}")
                else:
                    loc.asignar_guardia(dia, turno, g)

    return asignaciones
