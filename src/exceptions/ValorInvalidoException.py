class ValorInvalidoException(Exception):
    """
    Exceção que representa um erro quando um valor informado é inválido.
    """

    def __init__(self):
        super().__init__("O valor informado é inválido!")