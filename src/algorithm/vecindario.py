import random
from typing import List
from models.outputs import Asignacion

def swap_guardias_mismo_turno(asignaciones: List[Asignacion]) -> List[Asignacion]:
    nuevas = asignaciones.copy()
    if len(nuevas) < 2:
        return nuevas

    a1 = random.choice(nuevas)
    opciones = [
        a for a in nuevas
        if a.dia == a1.dia and a.turno == a1.turno and a.id_guardia != a1.id_guardia
    ]

    if not opciones:
        return nuevas

    a2 = random.choice(opciones)

    a1.id_guardia, a2.id_guardia = a2.id_guardia, a1.id_guardia
    a1.nombre_guardia, a2.nombre_guardia = a2.nombre_guardia, a1.nombre_guardia
    a1.tipo_guardia, a2.tipo_guardia = a2.tipo_guardia, a1.tipo_guardia
    a1.costo_turno, a2.costo_turno = a2.costo_turno, a1.costo_turno

    return nuevas

def reemplazar_ocasional_por_planta(asignaciones: List[Asignacion], guardias: List) -> List[Asignacion]:
    nuevas = asignaciones.copy()
    for a in nuevas:
        if a.tipo_guardia == "ocasional":
            for g in guardias:
                if g.tipo == "planta" and g.get_disponibilidad() >= 8:
                    if g.asignar_turno(8):
                        a.id_guardia = g.id
                        a.nombre_guardia = g.nombre
                        a.tipo_guardia = "planta"
                        a.costo_turno = g.costo_por_turno
                        break
    return nuevas

def mover_turno_guardia(asignaciones: List[Asignacion]) -> List[Asignacion]:
    nuevas = asignaciones.copy()
    a = random.choice(nuevas)
    turnos_disponibles = ["mañana", "tarde", "noche"]
    turnos_disponibles.remove(a.turno)
    nuevo_turno = random.choice(turnos_disponibles)
    a.turno = nuevo_turno
    return nuevas
