from clientes import *
import pytest


class Test_Cliente():

    def test_instanciar_cliente_cpf_vazio(self):
        
        with pytest.raises(Exception) as e:
            cliente = Cliente("","Levi", "sadfjadsuof")
        assert str(e.value) == 'CPF VAZIO'

    def test_instanciar_cliente_nome_vazio(self):
        
        with pytest.raises(Exception) as e:
            cliente = Cliente("13123124","", "sadfjadsuof")
        assert str(e.value) == 'NOME VAZIO'

    def test_instanciar_cliente_email_vazio(self):
        
        with pytest.raises(Exception) as e:
            cliente = Cliente("13123124","dsdsdsda", "")
        assert str(e.value) == 'EMAIL VAZIO'