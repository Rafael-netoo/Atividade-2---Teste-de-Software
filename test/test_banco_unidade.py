import unittest
from unittest.mock import Mock, patch
import sys
import os

# Adiciona src ao path para encontrar os módulos
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from src.negocio.Banco import Banco
from src.negocio.ContaEspecial import ContaEspecial
from src.negocio.ContaPoupanca import ContaPoupanca
from src.negocio.Cliente import Cliente
from src.exceptions.ContaJaCadastradaException import ContaJaCadastradaException
from src.exceptions.ContaNaoEncontradaException import ContaNaoEncontradaException
from src.exceptions.ClienteJaCadastradoException import ClienteJaCadastradoException
from src.exceptions.ClienteNaoCadastradoException import ClienteNaoCadastradoException
from src.exceptions.ContaJaAssociadaException import ContaJaAssociadaException
from src.exceptions.RenderBonusContaEspecialException import RenderBonusContaEspecialException
from src.exceptions.RenderJurosPoupancaException import RenderJurosPoupancaException
from src.exceptions.RepositorioException import RepositorioException
from src.exceptions.SaldoInsuficienteException import SaldoInsuficienteException
from src.exceptions.ValorInvalidoException import ValorInvalidoException
from src.exceptions.AtualizacaoNaoRealizadaException import AtualizacaoNaoRealizadaException

def get_banco_mock():
    repositorio_clientes = Mock()
    repositorio_contas = Mock()
    return Banco(repositorio_clientes, repositorio_contas)

class TesteBancoUnidade(unittest.TestCase):

    def setUp(self):
        self.banco = get_banco_mock()
        self.conta = Mock()  # Mock para ContaAbstrata
        self.conta_especial = ContaEspecial("2", 200.0)  # Instância concreta
        self.conta_poupanca = ContaPoupanca("3", 300.0)  # Instância concreta
        self.cliente = Cliente("123", "João")
        self.banco.clientes.getIterator = Mock(return_value=iter([]))  # Mock para iterador vazio
        self.conta.getNumero = Mock(return_value="1")
        self.conta_especial.getNumero = Mock(return_value="2")
        self.conta_poupanca.getNumero = Mock(return_value="3")

    def test_get_instance_com_sucesso(self):
        with patch('src.negocio.Banco.Banco') as mock_banco:
            mock_banco.return_value = self.banco
            result = Banco.get_instance()
            self.assertIsNotNone(result)

    def test_cadastrar_cliente_com_sucesso(self):
        self.banco.clientes.inserir.return_value = True
        self.banco.cadastrar_cliente(self.cliente)
        self.assertTrue(self.banco.clientes.inserir.called)

    def test_cadastrar_cliente_existente(self):
        self.banco.clientes.inserir.return_value = False
        with self.assertRaises(ClienteJaCadastradoException):
            self.banco.cadastrar_cliente(self.cliente)

    def test_procurar_cliente_com_sucesso(self):
        self.banco.clientes.procurar.return_value = self.cliente
        result = self.banco.procurar_cliente("123")
        self.assertEqual(self.cliente, result)

    def test_procurar_cliente_inexistente(self):
        self.banco.clientes.procurar.return_value = None
        result = self.banco.procurar_cliente("999")
        self.assertIsNone(result)

    def test_cadastrar_conta_com_sucesso(self):
        self.banco.contas.inserir.return_value = True
        self.banco.cadastrar_conta(self.conta)
        self.assertTrue(self.banco.contas.inserir.called)

    def test_cadastrar_conta_existente(self):
        self.banco.contas.inserir.return_value = False
        with self.assertRaises(ContaJaCadastradaException):
            self.banco.cadastrar_conta(self.conta)

    def test_procurar_conta_com_sucesso(self):
        self.banco.contas.procurar.return_value = self.conta
        result = self.banco.procurar_conta("1")
        self.assertEqual(self.conta, result)

    def test_procurar_conta_inexistente(self):
        self.banco.contas.procurar.return_value = None
        result = self.banco.procurar_conta("999")
        self.assertIsNone(result)

    def test_associar_conta_com_sucesso(self):
        self.banco.contas.procurar.return_value = self.conta
        self.banco.clientes.procurar.return_value = self.cliente
        self.cliente.adicionar_conta = Mock()
        self.banco.clientes.atualizar.return_value = True
        self.banco.associar_conta("123", "1")
        self.assertTrue(self.cliente.adicionar_conta.called)

    def test_associar_conta_inexistente(self):
        self.banco.contas.procurar.return_value = None
        with self.assertRaises(ContaNaoEncontradaException):
            self.banco.associar_conta("123", "1")

    def test_associar_conta_cliente_inexistente(self):
        self.banco.contas.procurar.return_value = self.conta
        self.banco.clientes.procurar.return_value = None
        with self.assertRaises(ClienteNaoCadastradoException):
            self.banco.associar_conta("999", "1")

    def test_associar_conta_ja_associada(self):
        self.banco.contas.procurar.return_value = self.conta
        self.banco.clientes.procurar.return_value = self.cliente
        self.banco.clientes.getIterator.return_value = [Mock(get_cpf=Mock(return_value="999"), get_contas=Mock(return_value={"1"}))]
        with self.assertRaises(ContaJaAssociadaException):
            self.banco.associar_conta("123", "1")

    def test_remover_cliente_com_sucesso(self):
        self.banco.clientes.procurar.return_value = self.cliente
        self.banco.clientes.remover.return_value = True
        self.cliente.get_contas = Mock(return_value=[])
        self.banco.remover_cliente("123")
        self.assertTrue(self.banco.clientes.remover.called)

    def test_remover_cliente_inexistente(self):
        self.banco.clientes.procurar.return_value = None
        with self.assertRaises(ClienteNaoCadastradoException):
            self.banco.remover_cliente("999")

    def test_remover_conta_com_sucesso(self):
        self.banco.clientes.procurar.return_value = self.cliente
        self.banco.contas.procurar.return_value = self.conta
        self.banco.contas.remover.return_value = True
        self.cliente.remover_conta = Mock()
        self.banco.remover_conta(self.cliente, "1")
        self.assertTrue(self.banco.contas.remover.called)

    def test_remover_conta_cliente_inexistente(self):
        self.banco.clientes.procurar.return_value = None
        with self.assertRaises(ClienteNaoCadastradoException):
            self.banco.remover_conta(self.cliente, "1")

    def test_remover_conta_inexistente(self):
        self.banco.clientes.procurar.return_value = self.cliente
        self.banco.contas.procurar.return_value = None
        with self.assertRaises(ContaNaoEncontradaException):
            self.banco.remover_conta(self.cliente, "1")

    def test_creditar_com_sucesso(self):
        self.conta.creditar = Mock()
        self.banco.contas.atualizar.return_value = True
        self.banco.creditar(self.conta, 50.0)
        self.assertTrue(self.conta.creditar.called)

    def test_creditar_valor_negativo(self):
        with self.assertRaises(ValorInvalidoException):
            self.banco.creditar(self.conta, -50.0)

    def test_debitar_com_sucesso(self):
        self.banco.contas.existe.return_value = True
        self.conta.debitar = Mock()
        self.banco.contas.atualizar.return_value = True
        self.banco.debitar(self.conta, 50.0)
        self.assertTrue(self.conta.debitar.called)

    def test_debitar_valor_negativo(self):
        with self.assertRaises(ValorInvalidoException):
            self.banco.debitar(self.conta, -50.0)

    def test_transferir_com_sucesso(self):
        conta_destino = Mock()
        conta_destino.getNumero.return_value = "2"
        self.banco.contas.existe.side_effect = lambda x: x in ["1", "2"]
        self.conta.debitar = Mock()
        conta_destino.creditar = Mock()
        self.banco.contas.atualizar.side_effect = lambda x: True
        self.banco.transferir(self.conta, conta_destino, 50.0)
        self.assertTrue(self.conta.debitar.called)
        self.assertTrue(conta_destino.creditar.called)

    def test_atualizar_cliente_com_sucesso(self):
        self.banco.clientes.atualizar.return_value = True
        self.banco.atualizar_cliente(self.cliente)
        self.assertTrue(self.banco.clientes.atualizar.called)

    def test_atualizar_cliente_falha(self):
        self.banco.clientes.atualizar.return_value = False
        with self.assertRaises(AtualizacaoNaoRealizadaException):
            self.banco.atualizar_cliente(self.cliente)

    def test_render_bonus_com_sucesso(self):
        self.banco.contas.existe.return_value = True
        self.conta_especial.renderbonus = Mock()
        self.banco.contas.atualizar.return_value = True
        self.banco.render_bonus(self.conta_especial)
        self.assertTrue(self.conta_especial.renderbonus.called)

    def test_render_bonus_conta_invalida(self):
        self.banco.contas.existe.return_value = True
        with self.assertRaises(RenderBonusContaEspecialException):
            self.banco.render_bonus(self.conta)

    def test_render_juros_com_sucesso(self):
        self.banco.contas.existe.return_value = True
        self.conta_poupanca.render_juros = Mock()
        self.banco.contas.atualizar.return_value = True
        self.banco.render_juros(self.conta_poupanca)
        self.assertTrue(self.conta_poupanca.render_juros.called)

    def test_render_juros_conta_invalida(self):
        self.banco.contas.existe.return_value = True
        with self.assertRaises(RenderJurosPoupancaException):
            self.banco.render_juros(self.conta)

if __name__ == '__main__':
    unittest.main()