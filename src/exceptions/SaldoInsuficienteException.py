class SaldoInsuficienteException(Exception):
    """
    Exceção que representa um erro no débito de um valor no saldo da conta.
    """

    def __init__(self, numero, saldo):
        super().__init__(f"Saldo insuficiente! O saldo atual da conta {numero} é R${saldo:.2f}")