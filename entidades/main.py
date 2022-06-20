from clientes import Cliente
from caixa import Caixa
from caixas import AtendimentoCaixas
from typing import List
from fila_atendimento import FilaAtendimento


class Agencia:

    def __init__(self, numero_de_caixas: int) -> None:
        self.caixas: AtendimentoCaixas = AtendimentoCaixas(numero_de_caixas)

    def atender_cliente(self) -> None:
        pass


agencia = Agencia()
agencia.atender_cliente()