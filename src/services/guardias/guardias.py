from ..nodo.nodo import Nodo

class Guardia(Nodo):
    def __init__(self, id: str, nombre: str, tipo: str, costo_por_turno: float, horas_max_semana: int = 0):
        super().__init__(id=id)
        self.nombre = nombre
        self.tipo = tipo
        self.costo_por_turno = costo_por_turno

    def __str__(self):
        return f"Guardia(id={self.id}, tipo={self.tipo}, costo={self.costo_por_turno})"
    
    def __repr__(self):
        return f"Guardia({self.id})"
