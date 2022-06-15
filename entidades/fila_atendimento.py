from typing import List
from clientes import Cliente


class FilaAtendimento():

    def __init__(self):
        self.fila_atendimento: List[int] = []

    def entrar(self, cliente: Cliente) -> None:
        self.fila_atendimento.append(cliente)

    def proximo(self) -> str:
        if len(self.fila_atendimento) == 0:
            return None
        return self.fila_atendimento.pop(0)
    
    def numero_de_clientes(self) -> int:
        return len(self.fila_atendimento)

