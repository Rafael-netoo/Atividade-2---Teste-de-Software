class EntradaInvalidaException(Exception):
    """
    Exceção que representa um erro na entrada de dados de um campo.
    """

    def __init__(self):
        super().__init__("Entrada inválida!")