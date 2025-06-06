from ..nodo.nodo import Nodo

class Guardia(Nodo):
    def __init__(self, id: str, nombre: str, tipo: str, costo_por_turno: float, horas_max_semana: int = 0):
        super().__init__(id=id)
        self.nombre = nombre
        self.tipo = tipo
        self.costo_por_turno = costo_por_turno
        self.horas_max_semana = horas_max_semana
        self.horas_asignadas = 0
        self.dias_asignados = set()

    def get_disponibilidad(self):
        return self.horas_max_semana - self.horas_asignadas
    
    def asignar_turno(self, dia: str, horas: int):
        if self.puede_asignar_turno(dia, horas):
            self.horas_asignadas += horas
            self.dias_asignados.add(dia)
            return True
        return False

    def puede_asignar_turno(self, dia: str, horas_turno: int = 8):
        return (
            self.horas_asignadas + horas_turno <= self.horas_max_semana and
            dia not in self.dias_asignados
        )

    def reset_horas(self):
        self.horas_asignadas = 0
        self.dias_asignados = set()

    def __str__(self):
        return f"Guardia(id={self.id}, tipo={self.tipo}, costo={self.costo_por_turno})"
