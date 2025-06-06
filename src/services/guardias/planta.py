from .guardias import Guardia

class GuardiaPlanta(Guardia):
    def __init__(self, id: str, nombre: str, costo_por_turno: float, horas_max_semana: int):
        super().__init__(
            id, 
            nombre, 
            "planta", 
            costo_por_turno
        )
        self.horas_max_semana = horas_max_semana
        self.horas_asignadas = 0

    def get_disponibilidad(self):
        return self.horas_max_semana - self.horas_asignadas
    
    def asignar_turno(self, horas: int):
        if self.get_disponibilidad() >= horas:
            self.horas_asignadas += horas
            return True
        return False

    def reset_horas(self):
        self.horas_asignadas = 0

    def __repr__(self):
        return f"GuardiaPlanta({self.id}, {self.vecinos})"