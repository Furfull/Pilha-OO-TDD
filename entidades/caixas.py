from clientes import Cliente
from caixa import Caixa
from typing import List
from fila_atendimento import FilaAtendimento


class AtendimentoCaixas():

    def __init__(self, numero_de_caixas: int):
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

    def finalizar_atendimento(self) -> None:
        for caixa in self.caixas:
            if caixa.atendendo():
                caixa.finalizar_atendimento()
                return
    
    def atender_fila(self) -> None:
        for caixa in self.caixas:
            if caixa.disponivel():
                caixa.atender_cliente(self.fila_atendimento.proximo())
                return

    def fechar_caixa(self, numero_caixa: int) -> None:
        for indice, caixa in enumerate(self.caixas):
            if indice == numero_caixa:
                caixa.fechar()
                return
    
    def abrir_caixa(self, numero_caixa: int) -> None:
        for indice, caixa in enumerate(self.caixas):
            if indice == numero_caixa:
                caixa.abrir()
                return

    def tamanho_caixas(self) -> int:
        return len(self.caixas)

    def tamanho_fila(self) -> int:
        return self.fila_atendimento.numero_de_clientes()
                

# atendimentocaixas = AtendimentoCaixas(5)
# cliente = Cliente("123", "Levi", "dkfndf")
# cliente2 = Cliente("1234", "Levi", "dkfndfds")

# #print(atendimentocaixas.teste())


# atendimentocaixas.atender_cliente(cliente)
# atendimentocaixas.atender_cliente(cliente)
# atendimentocaixas.atender_cliente(cliente)
# atendimentocaixas.atender_cliente(cliente)
# atendimentocaixas.atender_cliente(cliente)
# atendimentocaixas.atender_cliente(cliente)

# print(atendimentocaixas.caixas[0].cliente)

