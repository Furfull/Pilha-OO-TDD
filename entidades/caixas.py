from clientes import Cliente
from caixa import Caixa
from typing import List
from fila_atendimento import FilaAtendimento


class AtendimentoCaixas():

    def __init__(self, numero_de_caixas):
        self.fila_atendimento: FilaAtendimento = FilaAtendimento()
        self.caixas: List[Caixa] = [] 
        for i in range(numero_de_caixas):
            self.caixas.append(Caixa())
        self.teste = 0

    def atender_cliente(self, cliente: Cliente) -> None:
        for caixa in self.caixas:
            if caixa.disponivel():
                caixa.atender_cliente(cliente)
                return 
        self.fila_atendimento.entrar(cliente)
        return self.fila_atendimento.fila_atendimento


atendimentocaixas = AtendimentoCaixas(5)
cliente = Cliente("123", "Levi", "dkfndf")
cliente2 = Cliente("1234", "Levi", "dkfndfds")

#print(atendimentocaixas.teste())


atendimentocaixas.atender_cliente(cliente)
atendimentocaixas.atender_cliente(cliente)
atendimentocaixas.atender_cliente(cliente)
atendimentocaixas.atender_cliente(cliente)
atendimentocaixas.atender_cliente(cliente)
atendimentocaixas.atender_cliente(cliente)

print(atendimentocaixas.atender_cliente(cliente2))

