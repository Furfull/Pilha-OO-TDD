from caixa import Caixa


def test_criar_caixas_ok() -> None:
    caixa = Caixa()
    retorno = caixa.criar_caixas(3)
    assert retorno == [(0, 1), (0, 1), (0, 1)]

def test_criar_caixas_add_ok() -> None:
    caixa = Caixa()
    caixa.criar_caixas(3)
    retorno = caixa.criar_caixas(3)
    assert retorno == [(0, 1), (0, 1), (0, 1), (0, 1), (0, 1), (0, 1)]

def test_atender_cliente_ok() -> None:
    caixa = Caixa()
    caixa.criar_caixas(3)
    retorno = caixa.atender_cliente()
    assert retorno == ('ATENDIDO', [(1, 1), (0, 1), (0, 1)])

def test_atender_cliente_fila() -> None:
    caixa = Caixa()
    caixa.criar_caixas(3)
    caixa.atender_cliente()
    caixa.atender_cliente()
    caixa.atender_cliente()
    retorno = caixa.atender_cliente()
    assert retorno == [1]

def test_finalizar_atendimento_ok() -> None:
    caixa = Caixa()
    caixa.criar_caixas(3)
    caixa.atender_cliente()
    retorno = caixa.finalizar_atendimento(0)
    assert retorno == 'ATENDIMENTO FINALIZADO'

def test_finalizar_atendimento_caixa_vazio() -> None:
    caixa = Caixa()
    caixa.criar_caixas(3)
    caixa.atender_cliente()
    retorno = caixa.finalizar_atendimento(2)
    assert retorno == 'CAIXA VAZIO'

def test_abrir_caixa_erro_ja_aberto() -> None:
    caixa = Caixa()
    caixa.criar_caixas(3)
    retorno = caixa.abrir_caixa(1)
    assert retorno == 'Caixa 1 já está aberto'

def test_abrir_caixa_erro_caixa_nao_existe() -> None:
    caixa = Caixa()
    caixa.criar_caixas(3)
    retorno = caixa.abrir_caixa(4)
    assert retorno == 'Caixa 4 não existe'

def test_abrir_caixa_ok() -> None:
    caixa = Caixa()
    caixa.criar_caixas(3)
    caixa.fechar_caixa(1)
    retorno = caixa.abrir_caixa(1)
    assert retorno == 'Caixa 1 aberto com sucesso'

def test_fechar_caixa_ok() -> None:
    caixa = Caixa()
    caixa.criar_caixas(3)
    retorno = caixa.fechar_caixa(1)
    assert retorno == 'Caixa 1 fechado com sucesso'

def test_fechar_caixa_erro_caixa_nao_existe() -> None:
    caixa = Caixa()
    caixa.criar_caixas(3)
    retorno = caixa.fechar_caixa(4)
    assert retorno == 'Caixa 4 não existe'

def test_fechar_caixa_ok() -> None:
    caixa = Caixa()
    caixa.criar_caixas(3)
    caixa.atender_cliente()
    retorno = caixa.fechar_caixa(0)
    assert retorno == 'Caixa 0 já está fechado ou está em atendimento'