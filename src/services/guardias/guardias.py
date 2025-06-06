from ..nodo.nodo import Nodo

class Guardia(Nodo):
    def __init__(self, id: str, nombre: str, tipo: str, costo_por_turno: float, horas_max_semana: int = 0):
        super().__init__(id=id)
        self.nombre = nombre
        self.tipo = tipo
        self.costo_por_turno = costo_por_turno
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

    def __str__(self):
        return f"Guardia(id={self.id}, tipo={self.tipo}, costo={self.costo_por_turno})"
