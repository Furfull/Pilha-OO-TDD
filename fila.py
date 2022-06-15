from typing import List


class Fila():

    def __init__(self):
        self.fila: List[int] = []
        self.ticket: int = 1

    def entrar_fila(self) -> List[int]:
        self.fila.append(self.ticket)
        self.ticket+=1
        return self.fila

    def sair_fila(self) -> List[int]:
        if len(self.fila) > 0:
            self.fila.pop(0)
            return self.fila
        if len(self.fila) == 0:
            return 'não há clientes na fila'
