class ClienteJaPossuiContaException(Exception):
    """
    Exceção que representa um erro na associação de uma conta que o cliente já
    possui a ele mesmo.
    """

    def __init__(self):
        super().__init__("O cliente já possui esta conta associada a ele!")