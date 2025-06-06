from .guardias import Guardia

class GuardiaOcasional(Guardia):
    def __init__(self, id: str, nombre: str, costo_por_turno: float = 47000):
        super().__init__(
            id, 
            nombre, 
            "ocasional", 
            costo_por_turno, 
            horas_max_semana=0
        )
