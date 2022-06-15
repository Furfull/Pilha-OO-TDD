from typing import List, Tuple
from fila import Fila
from constantes import CAIXA, SEMCLIENTEINATIVO, COMCLIENTEATIVO, COMCLIENTEINATIVO


class Caixa():

    def __init__(self):
        self.atendimento: int = 0
        self.conformacao: int = 1
        self.caixas: List[int] = []
        self.fila = Fila()

    def adicionar_caixas(self, numero_de_caixas: int) -> List[Tuple[int]]:
        for i in range(numero_de_caixas): 
            self.caixas.append((self.atendimento, self.conformacao))
        return self.caixas

    def criar_caixas(self, numero_de_caixas: int) -> List[Tuple[int]]:
        self.caixas = [(self.atendimento, self.conformacao)] * (
            numero_de_caixas)
        return self.caixas
    
    def caixa_ativo_atendendo():
        pass

    def caixa_inativo():
        pass

    def caixa_ativo_nao_atendendo():
        pass

    def atender_cliente(self) -> str:
        for caixa,valor in enumerate(self.caixas):
            if valor[0] == 0:
                self.caixas[caixa] = COMCLIENTEATIVO
                return "ATENDIDO", self.caixas
        if COMCLIENTEINATIVO not in self.caixas:
            return self.fila.entrar_fila()
    
    def finalizar_atendimento(self, numero_caixa: int) -> int:
        if self.caixas[numero_caixa] == COMCLIENTEATIVO:
            self.caixas[numero_caixa] = COMCLIENTEINATIVO
            return 'ATENDIMENTO FINALIZADO'
        else:
            return 'CAIXA VAZIO'
    
    def abrir_caixa(self, numero_caixa: int) -> str:
        if numero_caixa > len(self.caixas)-1:
            return f'{CAIXA} {numero_caixa} não existe'
        if self.caixas[numero_caixa] == SEMCLIENTEINATIVO:
            self.caixas[numero_caixa] = COMCLIENTEINATIVO
            return f'{CAIXA} {numero_caixa} aberto com sucesso'
        if self.caixas[numero_caixa] == COMCLIENTEINATIVO or (
            self.caixas[numero_caixa] == COMCLIENTEATIVO
        ):
            return f'{CAIXA} {numero_caixa} já está aberto'
    
    def fechar_caixa(self, numero_caixa: int) -> str:
        if numero_caixa > len(self.caixas)-1:
            return f'{CAIXA} {numero_caixa} não existe'
        if self.caixas[numero_caixa] == COMCLIENTEINATIVO:
            self.caixas[numero_caixa] = SEMCLIENTEINATIVO
            return f'{CAIXA} {numero_caixa} fechado com sucesso'
        if self.caixas[numero_caixa] == SEMCLIENTEINATIVO or (
            self.caixas[numero_caixa] == COMCLIENTEATIVO
        ):
            return f'{CAIXA} {numero_caixa} já fechado ou está em atendimento'
        
    def estatisticas(self):
        pass

caixa = Caixa()
print(caixa.criar_caixas(3))
print(caixa.atender_cliente())
print(caixa.atender_cliente())
print(caixa.atender_cliente())
print(caixa.atender_cliente())
print(caixa.atender_cliente())
print(caixa.atender_cliente())
print(caixa.finalizar_atendimento(1))
print(caixa.fechar_caixa(1))
print(caixa.abrir_caixa(5))
print(caixa.caixas)