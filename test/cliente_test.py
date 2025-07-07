from src.negocio.Cliente import Cliente

import unittest

class test_cliente_cpf(unittest.TestCase):
    def test_cliente_cpf(self):
        cliente = Cliente("João", "12345678900")
        self.assertEqual(cliente.get_cpf(), "12345678900", msg= "O CPF do cliente deveria ser 12345678900")

class test_cliente_nome(unittest.TestCase):
    def test_cliente_nome(self):
        cliente = Cliente("João", "12345678900")
        self.assertEqual(cliente.get_nome(), "João", msg= "O nome do cliente deveria ser João")

class test_cliente_contas(unittest.TestCase):
    def test_cliente_contas(self):
        cliente = Cliente("João", "12345678900")
        self.assertEqual(cliente.get_contas(), [], msg= "O cliente não deveria possuir contas")

class test_cliente_adicionar_conta(unittest.TestCase):
    def test_cliente_adicionar_conta(self):
        cliente = Cliente("João", "12345678900")
        cliente.adicionar_conta("123")
        self.assertEqual(cliente.get_contas(), ["123"], msg= "O cliente deveria possuir a conta 123")

class test_cliente_remover_conta(unittest.TestCase):
    def test_cliente_remover_conta(self):
        cliente = Cliente("João", "12345678900")
        cliente.adicionar_conta("123")
        cliente.remover_conta("123")
        self.assertEqual(cliente.get_contas(), [], msg= "O cliente não deveria possuir contas")

class test_cliente_remover_todas_as_contas(unittest.TestCase):
    def test_cliente_remover_todas_as_contas(self):
        cliente = Cliente("João", "12345678900")
        cliente.adicionar_conta("123")
        cliente.adicionar_conta("456")
        cliente.remover_todas_as_contas()
        self.assertEqual(cliente.get_contas(), [], msg= "O cliente não deveria possuir contas")

def runClienteTests():
    suite =        unittest.defaultTestLoader.loadTestsFromTestCase(test_cliente_cpf)
    suite.addTests(unittest.defaultTestLoader.loadTestsFromTestCase(test_cliente_nome))
    suite.addTests(unittest.defaultTestLoader.loadTestsFromTestCase(test_cliente_contas))
    suite.addTests(unittest.defaultTestLoader.loadTestsFromTestCase(test_cliente_adicionar_conta))
    suite.addTests(unittest.defaultTestLoader.loadTestsFromTestCase(test_cliente_remover_conta))
    suite.addTests(unittest.defaultTestLoader.loadTestsFromTestCase(test_cliente_remover_todas_as_contas))
    unittest.TextTestRunner(verbosity=2, failfast=True).run(suite)

if __name__ == '__main__':
    runClienteTests()