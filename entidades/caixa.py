from typing import List, Tuple
from status_caixa_enum import StatusCaixaEnum
from clientes import Cliente


class Caixa:

    def __init__(self):
        self.status: StatusCaixaEnum = StatusCaixaEnum.DISPONIVEL
        self.cliente = None

    def atender_cliente(self, cliente: Cliente) -> str:
        if self.status != StatusCaixaEnum.DISPONIVEL:
            return 'CAIXA NAO DISPONIVEL OU OCUPADO'
        self.cliente = cliente
        self.status = StatusCaixaEnum.EM_ATENDIMENTO
        return 'OK'

    def finalizar_atendimento(self) -> str:
        if self.status != StatusCaixaEnum.EM_ATENDIMENTO:
            return 'CAIXA NAO ESTA EM ATENDIMENTO OU DISPONIVEL'
        self.cliente = None
        self.status = StatusCaixaEnum.DISPONIVEL
        return 'OK'

    def abrir(self) -> str:
        if self.status != StatusCaixaEnum.INATIVO:
            return 'CAIXA NAO ESTA FECHADO'
        self.cliente = None
        self.status = StatusCaixaEnum.DISPONIVEL
        return 'OK'

    def fechar(self) -> str:
        if self.status == StatusCaixaEnum.EM_ATENDIMENTO:
            return 'CAIXA EM ATENDIMENTO'
        if self.status == StatusCaixaEnum.INATIVO:
            return 'CAIXA JA ESTA FECHADO'
        self.cliente = None
        self.status = StatusCaixaEnum.INATIVO
        return 'OK'
    
    def disponivel(self) -> bool:
        return self.status == StatusCaixaEnum.DISPONIVEL

    def atendendo(self) -> bool:
        return self.status == StatusCaixaEnum.EM_ATENDIMENTO
