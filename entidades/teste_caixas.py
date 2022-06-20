from caixas import AtendimentoCaixas
from clientes import Cliente
from caixa import Caixa


class TestAtendimentoCaixas:

    def test_atender_cliente_ok(self):
        atendimentocaixas = AtendimentoCaixas(2)
        cliente = Cliente("123", "Levi", "dkfndf")
        cliente2 = Cliente("1234", "Levi", "dkfndfds")
        atendimentocaixas.atender_cliente(cliente)
        atendimentocaixas.atender_cliente(cliente2)
        atendimentocaixas.caixas[0]
        return 