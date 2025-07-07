class ContaJaAssociadaException(Exception):
    """
    Exceção que representa um erro na associação de uma conta a um cliente que
    já possui a conta.
    """

    def __init__(self):
        super().__init__("Número de conta já associada a um cliente!")