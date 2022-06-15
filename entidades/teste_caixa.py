from caixa import Caixa
from clientes import Cliente


class TestCaixa:

    def test_atender_cliente_ok(self) -> None:
        caixa = Caixa()
        cliente = Cliente("123", "Levi", "dkfndf")
        retorno = caixa.atender_cliente(cliente)
        assert retorno == 'OK'

    def test_atender_cliente_erro_caixa_em_atendimento(self) -> None:
        caixa = Caixa()
        cliente = Cliente("123", "Levi", "dkfndf")
        cliente2 = Cliente("123", "Levi", "dkfndf")
        caixa.atender_cliente(cliente)
        retorno = caixa.atender_cliente(cliente2)
        assert retorno == 'CAIXA NAO DISPONIVEL OU OCUPADO'

    def test_atender_cliente_erro_caixa_inativo(self) -> None:
        caixa = Caixa()
        caixa.fechar()
        cliente = Cliente("123", "Levi", "dkfndf")
        retorno = caixa.atender_cliente(cliente)
        assert retorno == 'CAIXA NAO DISPONIVEL OU OCUPADO'

    def test_finalizar_atendimento_ok(self) -> None:
        caixa = Caixa()
        cliente = Cliente("123", "Levi", "dkfndf")
        caixa.atender_cliente(cliente)
        retorno = caixa.finalizar_atendimento()
        assert retorno == 'OK'

    def test_finalizar_atendimento_caixa_disponivel(self) -> None:
        caixa = Caixa()
        retorno = caixa.finalizar_atendimento()
        assert retorno == 'CAIXA NAO ESTA EM ATENDIMENTO OU DISPONIVEL'

    def test_finalizar_atendimento_caixa_inativo(self) -> None:
        caixa = Caixa()
        caixa.fechar()
        retorno = caixa.finalizar_atendimento()
        assert retorno == 'CAIXA NAO ESTA EM ATENDIMENTO OU DISPONIVEL'
    
    def test_abrir_ok(self) -> None:
        caixa = Caixa()
        caixa.fechar()
        retorno = caixa.abrir()
        assert retorno == 'OK'

    def test_abrir_erro_caixa_disponivel(self) -> None:
        caixa = Caixa()
        retorno = caixa.abrir()
        assert retorno == 'CAIXA NAO ESTA FECHADO'

    def test_abrir_erro_caixa_em_atendimento(self) -> None:
        caixa = Caixa()
        cliente = Cliente("123", "Levi", "dkfndf")
        caixa.atender_cliente(cliente)
        retorno = caixa.abrir()
        assert retorno == 'CAIXA NAO ESTA FECHADO'

    def test_fechar_ok(self) -> None:
        caixa = Caixa()
        retorno = caixa.fechar()
        assert retorno == 'OK'

    def test_fechar_caixa_em_atendimento(self) -> None:
        caixa = Caixa()
        cliente = Cliente("123", "Levi", "dkfndf")
        caixa.atender_cliente(cliente)
        retorno = caixa.fechar()
        assert retorno == 'CAIXA EM ATENDIMENTO'

    def test_fechar_caixa_inativo(self) -> None:
        caixa = Caixa()
        caixa.fechar()
        retorno = caixa.fechar()
        assert retorno == 'CAIXA JA ESTA FECHADO'