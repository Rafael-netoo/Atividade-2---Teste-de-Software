import unittest
from src.dados.RepositorioClientesArquivoDB import RepositorioClientesArquivoDB
from mockito import when, mock, unstub

from src.negocio.Cliente import Cliente


class test_listar_contas(unittest.TestCase):
    def test_listar_contas(self):
        
        # Mockar o objeto Database
        rep = RepositorioClientesArquivoDB()
        mock_clients = [Cliente('123', 'Teste'), Cliente('321', 'Teste2')]
        when(rep).listar_clientes().thenReturn(mock_clients)
        
        # Chamar o método que foi mockado
        result = rep.listar_clientes()
        
        # Garantir que o método retornou o resultado esperado
        self.assertEqual(result, [Cliente('123', 'Teste'), Cliente('321', 'Teste2')])

        # Retirar o mock do objeto
        unstub()

class test_atualizar_conta(unittest.TestCase):
    def test_atualizar_conta(self):
        
        # Mockar o objeto Database
        rep = RepositorioClientesArquivoDB()
        mock_client = Cliente('123', 'Nome Inicial Da Silva')
        when(rep).atualizar(mock_client).thenReturn(True)
        
        # Chamar o método que foi mockado
        result = rep.atualizar(mock_client)
        
        # Garantir que o método retornou o resultado esperado
        self.assertEqual(result, True)
        
        # Retirar o mock do objeto
        unstub()

def runMockitoTests():
    suite =        unittest.defaultTestLoader.loadTestsFromTestCase(test_listar_contas)
    suite.addTests(unittest.defaultTestLoader.loadTestsFromTestCase(test_atualizar_conta))
    unittest.TextTestRunner(verbosity=2, failfast=True).run(suite)
    
if __name__ == '__main__':
    runMockitoTests()