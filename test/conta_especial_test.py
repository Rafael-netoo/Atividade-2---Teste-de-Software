from src.exceptions.SaldoInsuficienteException import SaldoInsuficienteException
from src.negocio.ContaEspecial import ContaEspecial

import unittest

class test_conta_especial_debito(unittest.TestCase):
    def test_conta_especial_debito(self):
        conta = ContaEspecial("123", 100.0)
        conta.debitar(50.0)
        self.assertEqual(conta.getSaldo(), 50.0, msg= "O saldo da conta deveria ser 50.0")

class test_conta_especial_debito_saldo_insuficiente(unittest.TestCase):
    def test_conta_especial_debito_saldo_insuficiente(self):
        conta = ContaEspecial("123", 100.0)
        with self.assertRaises(SaldoInsuficienteException):
            conta.debitar(150.0)

class test_conta_especial_numero(unittest.TestCase):
    def test_conta_especial_numero(self):
        conta = ContaEspecial("123", 100.0)
        self.assertEqual(conta.getNumero(), "123", msg= "O número da conta deveria ser 123")

class test_conta_especial_saldo_inicial_negativo(unittest.TestCase):
    def test_conta_especial_saldo_inicial_negativo(self):
        conta = ContaEspecial("123", -100.0)
        self.assertEqual(conta.getSaldo(), 0.0, msg= "O saldo da conta deveria ser 0.0")

def runContaEspecialTests():
    suite =        unittest.defaultTestLoader.loadTestsFromTestCase(test_conta_especial_debito)
    suite.addTests(unittest.defaultTestLoader.loadTestsFromTestCase(test_conta_especial_debito_saldo_insuficiente))
    suite.addTests(unittest.defaultTestLoader.loadTestsFromTestCase(test_conta_especial_numero))
    suite.addTests(unittest.defaultTestLoader.loadTestsFromTestCase(test_conta_especial_saldo_inicial_negativo))
    unittest.TextTestRunner(verbosity=2, failfast=True).run(suite)

if __name__ == '__main__':
    runContaEspecialTests()