from src.exceptions.SaldoInsuficienteException import SaldoInsuficienteException
from src.negocio.ContaAbstrata import ContaAbstrata


class ContaImposto(ContaAbstrata):
    """
    Conta bancária do tipo conta imposto.
    """

    # Valor fixo do CPMFa
    CPMF = 0.0038

    def __init__(self, numero: str, saldo: float):
        """
        Inicializa uma conta do tipo imposto.

        :param numero: Número da conta.
        :param saldo: Saldo inicial da conta.
        """
        super().__init__(numero, saldo)

    def debitar(self, valor: float):
        """
        Debita um valor da conta, incluindo o imposto CPMF.

        :param valor: Valor a ser debitado.
        :raises SaldoInsuficienteException: Se o saldo for insuficiente para o débito e o imposto.
        """
        if self.getSaldo() < valor:
            raise SaldoInsuficienteException(self.getNumero(), self.getSaldo())

        # Calcula o imposto e o valor total a debitar
        imposto = valor * self.CPMF
        total = valor + imposto

        # Debita o total do saldo
        self.setSaldo(self.getSaldo() - total)

    #METODO ADICIONAL
    def get_tipo(self):
        return "imposto"
