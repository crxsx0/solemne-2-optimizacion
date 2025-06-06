from .guardias import Guardia

class GuardiaPlanta(Guardia):
    def __init__(self, id: str, nombre: str, costo_por_turno: float, horas_max_semana: int):
        super().__init__(
            id, 
            nombre, 
            "planta", 
            costo_por_turno, 
            horas_max_semana
        )
