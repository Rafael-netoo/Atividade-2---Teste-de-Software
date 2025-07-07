from src.exceptions.SaldoInsuficienteException import SaldoInsuficienteException
from src.negocio.ContaImposto import ContaImposto

import unittest

class test_conta_imposto_debito(unittest.TestCase):
    def test_conta_imposto_debito(self):
        conta = ContaImposto("123", 100.0)
        conta.debitar(50.0)
        self.assertEqual(conta.getSaldo(), 49.81, msg= "O saldo da conta deveria ser 49.81")

class test_conta_imposto_debito_saldo_insuficiente(unittest.TestCase):
    def test_conta_imposto_debito_saldo_insuficiente(self):
        conta = ContaImposto("123", 100.0)
        with self.assertRaises(SaldoInsuficienteException):
            conta.debitar(150.0)

class test_conta_imposto_numero(unittest.TestCase):
    def test_conta_imposto_numero(self):
        conta = ContaImposto("123", 100.0)
        self.assertEqual(conta.getNumero(), "123", msg= "O número da conta deveria ser 123")

class test_conta_imposto_saldo_inicial_negativo(unittest.TestCase):
    def test_conta_imposto_saldo_inicial_negativo(self):
        conta = ContaImposto("123", -100.0)
        self.assertEqual(conta.getSaldo(), 0.0, msg= "O saldo da conta deveria ser 0.0")

def runContaImpostoTests():
    suite =        unittest.defaultTestLoader.loadTestsFromTestCase(test_conta_imposto_debito)
    suite.addTests(unittest.defaultTestLoader.loadTestsFromTestCase(test_conta_imposto_debito_saldo_insuficiente))
    suite.addTests(unittest.defaultTestLoader.loadTestsFromTestCase(test_conta_imposto_numero))
    suite.addTests(unittest.defaultTestLoader.loadTestsFromTestCase(test_conta_imposto_saldo_inicial_negativo))
    unittest.TextTestRunner(verbosity=2, failfast=True).run(suite)

if __name__ == '__main__':
    runContaImpostoTests()