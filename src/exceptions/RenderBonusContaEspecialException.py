class RenderBonusContaEspecialException(Exception):
    """
    Exceção que representa um erro no método render bônus de conta especial.
    """

    def __init__(self):
        super().__init__("Erro ao render bônus, o número informado não é de uma Conta Especial!")