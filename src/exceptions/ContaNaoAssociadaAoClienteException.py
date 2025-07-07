class ContaNaoAssociadaAoClienteException(Exception):
    """
    Exceção que representa um erro na operação de uma conta associada ao
    cliente.
    """

    def __init__(self):
        super().__init__("O cliente não possui essa conta!")