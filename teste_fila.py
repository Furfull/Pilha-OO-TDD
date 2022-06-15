from fila import Fila


def test_entrar_fila() -> None:
    fila = Fila()
    retorno = fila.entrar_fila()
    assert retorno == [1]

def test_sair_fila_ok() -> None:
    fila = Fila()
    fila.entrar_fila()
    retorno = fila.sair_fila()
    assert retorno == []
    
def test_sair_fila_erro() -> None:
    fila = Fila()
    retorno = fila.sair_fila()
    assert retorno == 'não há clientes na fila'