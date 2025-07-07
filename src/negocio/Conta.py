from src.exceptions.SaldoInsuficienteException import SaldoInsuficienteException
from src.negocio.ContaAbstrata import ContaAbstrata

class Conta(ContaAbstrata):
    """
    Conta bancária do tipo conta normal.
    """

    def __init__(self, numero: float, valor: float):
        super().__init__(numero, valor)
        if valor < 0:
            self.setSaldo(0)

    def debitar(self, valor: float):
        if self.getSaldo() < valor:
            raise SaldoInsuficienteException(self.getNumero(), self.getSaldo())
        self.setSaldo(self.getSaldo() - valor)

    #METODO ADICIONAL
    def get_tipo(self):
        return "normal"