from caixas import AtendimentoCaixas
from clientes import Cliente
from caixa import Caixa


class TestAtendimentoCaixas:

    def test_atender_cliente_ok(self) -> None:
        atendimentocaixas = AtendimentoCaixas(2)
        cliente = Cliente("123", "Levi", "dkfndf")
        cliente2 = Cliente("1234", "Levi", "dkfndfds")
        cliente3 = Cliente("12345", "Levi", "dkfndfdfds")
        atendimentocaixas.atender_cliente(cliente)
        atendimentocaixas.atender_cliente(cliente2)
        atendimentocaixas.atender_cliente(cliente3)
        retorno = atendimentocaixas.tamanho_caixas()
        retorno2 = atendimentocaixas.tamanho_fila()
        assert retorno == 2 
        assert retorno2 == 1

    def test_atender_cliente_erro(self) -> None:
        atendimentocaixas = AtendimentoCaixas(2)
        cliente = Cliente("123", "Levi", "dkfndf")
        cliente2 = Cliente("1234", "Levi", "dkfndfds")
        cliente3 = Cliente("1234r5", "Levi", "dkfndfdfds")
        atendimentocaixas.atender_cliente(cliente)
        atendimentocaixas.atender_cliente(cliente2)
        atendimentocaixas.finalizar_atendimento()
        atendimentocaixas.atender_cliente(cliente3)
        retorno = atendimentocaixas.tamanho_fila()     
        assert retorno == 0

    def test_atender_fila_ok(self):
        atendimentocaixas = AtendimentoCaixas(2)
        cliente = Cliente("123", "Levi", "dkfndf")
        cliente2 = Cliente("1234", "Levi", "dkfndfds")
        cliente3 = Cliente("1234r5", "Levi", "dkfndfdfds")
        atendimentocaixas.atender_cliente(cliente)
        atendimentocaixas.atender_cliente(cliente2)
        atendimentocaixas.finalizar_atendimento()
        atendimentocaixas.atender_fila()
        assert atendimentocaixas.tamanho_fila() == 0

