from ..guardias.guardias import Guardia
from ..locaciones.locacion import Locacion
from ..nodo.nodo import Nodo

class Grafo:
    def __init__(self):
        self.nodos = {}

    def agregar_nodo(self, nodo: Nodo):
        self.nodos[nodo.id] = nodo

    def conectar(self, guardia: Guardia, locacion: Locacion, tiempo: float, max_tiempo: float = 2.5):
        if guardia.tipo == "planta" and tiempo < max_tiempo:
            guardia.conectar(locacion, tiempo)
            locacion.conectar(guardia, tiempo)
            
    def obtener_nodos(self) -> list:
        return list(self.nodos.values())

    def obtener_guardias(self) -> list:
        return [n for n in self.nodos.values() if isinstance(n, Guardia)]

    def obtener_locaciones(self) -> list:
        return [n for n in self.nodos.values() if isinstance(n, Locacion)]

    def vecinos_de(self, nodo_id: str) -> dict:
        return self.nodos[nodo_id].vecinos

    def __repr__(self):
        return f"Grafo con {len(self.nodos)} nodos"
