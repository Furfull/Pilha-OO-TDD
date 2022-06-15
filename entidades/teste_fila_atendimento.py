from fila_atendimento import FilaAtendimento
from clientes import Cliente


class TestFilaAtendimento:

    def test_entrar_ok(self):
        cliente = Cliente("123", "Levi", "dkfndf")
        fila_atendimento = FilaAtendimento()
        fila_atendimento.entrar(cliente)
        assert fila_atendimento.numero_de_clientes() == 1

    def test_proximo_ok(self):
        cliente = Cliente("123", "Levi", "dkfndf")
        fila_atendimento = FilaAtendimento()
        fila_atendimento.entrar(cliente)
        retorno = fila_atendimento.proximo()
        assert retorno.cpf == cliente.cpf
        assert fila_atendimento.numero_de_clientes() == 0

    def test_proximo_erro(self):
        fila_atendimento = FilaAtendimento()
        retorno = fila_atendimento.proximo()
        assert retorno == None
