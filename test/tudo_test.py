from test.conta_test import runContaTests
from test.conta_especial_test import runContaEspecialTests
from test.conta_imposto_test import runContaImpostoTests

from test.cliente_test import runClienteTests

def runAllTests():
    print("-*"*30, "\n", "Rodando todos os testes referentes a classe Conta\n", "-*"*30)
    runContaTests()
    print("-*"*30, "\n", "Fim dos testes referentes a classe Conta\n", "-*"*30, "\n")

    print("-*"*30, "\n", "Rodando todos os testes referentes a classe Conta Especial\n", "-*"*30)
    runContaEspecialTests()
    print("-*"*30, "\n", "Fim dos testes referentes a classe Conta Especial\n", "-*"*30, "\n")
    
    print("-*"*30, "\n", "Rodando todos os testes referentes a classe Conta Imposto\n", "-*"*30)
    runContaImpostoTests()
    print("-*"*30, "\n", "Fim dos testes referentes a classe Conta Imposto\n", "-*"*30, "\n")
    
    print("-*"*30, "\n", "Rodando todos os testes referentes a classe Cliente\n", "-*"*30)
    runClienteTests()
    print("-*"*30, "\n", "Fim dos testes referentes a classe Cliente\n", "-*"*30, "\n")
    
if __name__ == '__main__':
    runAllTests()