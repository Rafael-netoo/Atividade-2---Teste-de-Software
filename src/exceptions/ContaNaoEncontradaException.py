class ContaNaoEncontradaException(Exception):
    """
    Exceção que representa um erro caso o sistema tente encontrar uma conta não
    cadastrada.
    """

    def __init__(self):
        super().__init__("Conta não encontrada!")