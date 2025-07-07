class ContasOrigemDestinoIguaisException(Exception):
    """
    Exceção que representa um erro na tentativa de transferir um valor de uma
    conta de origem para uma conta de destino com o mesmo número.
    """

    def __init__(self):
        super().__init__("A conta de destino não pode ser igual à conta de origem!")