class RenderJurosPoupancaException(Exception):
    """
    Exceção que representa um erro no método render juros de conta poupança.
    """

    def __init__(self):
        super().__init__("Erro ao render juros, o número informado não é de uma Poupança!")