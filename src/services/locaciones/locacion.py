from ..nodo.nodo import Nodo
from ..guardias.guardias import Guardia

class Locacion(Nodo):
    def __init__(self, id: int, nombre: str, turnos: list[str] = None):
        super().__init__(id)
        self.nombre = nombre
        self.turnos = turnos
        self.cobertura = {dia: {turno: [] for turno in turnos} for dia in ["lunes", "martes", "miércoles", "jueves", "viernes", "sábado", "domingo"]}

    def __repr__(self):
        return f"Locacion(id={self.id}, nombre={self.nombre}, turnos={self.turnos})"

    def asignar_guardia(self, dia: str, turno: str, guardia: Guardia):
        self.cobertura[dia][turno].append(guardia.id)

    def turno_cubierto(self, dia: str, turno: str) -> bool:
        return len(self.cobertura[dia][turno]) >= self.demanda_diaria

    def faltan_guardias(self, dia: str, turno: str) -> int:
        return max(0, self.demanda_diaria - len(self.cobertura[dia][turno]))

    def resetear_cobertura(self):
        for dia in self.cobertura:
            for turno in self.turnos:
                self.cobertura[dia][turno] = []
