class CampoVazioException(Exception):
    """
    Exceção que representa um erro ao submeter um campo de texto vazio.
    """

    def __init__(self, valor):
        super().__init__(f"O campo {valor} não foi preenchido!")