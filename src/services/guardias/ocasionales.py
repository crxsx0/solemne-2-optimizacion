from .guardias import Guardia

class GuardiaOcasional(Guardia):
    def __init__(self, id: str, nombre: str, costo_por_turno: float = 47000):
        super().__init__(
            id, 
            nombre, 
            "ocasional", 
            costo_por_turno
        )
        self.hora_diarias_max = 8
        self.horas_asignadas = 0

    def get_disponibilidad(self):
        return self.hora_diarias_max - self.horas_asignadas
    def asignar_turno(self, horas: int):
        if self.get_disponibilidad() >= horas:
            self.horas_asignadas += horas
            return True
        return False
    def reset_horas(self):
        self.horas_asignadas = 0
    def __repr__(self):
        return f"GuardiaOcasional({self.id}, {self.vecinos})"
