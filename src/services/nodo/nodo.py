class Nodo:
    def __init__(self, id: int):
        self.id = id
        self.vecinos = {}

    def conectar(self, otro_nodo, peso: float):
        self.vecinos[otro_nodo.id] = peso

    def __repr__(self):
        return f"Nodo(id={self.id}, vecinos={list(self.vecinos.keys())})"