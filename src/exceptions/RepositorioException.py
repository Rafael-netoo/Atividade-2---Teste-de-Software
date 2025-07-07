class RepositorioException(Exception):
    """
    Exceção que representa erros de acesso a um meio de armazenamento
    persistente.
    """

    def __init__(self, mensagem=None, exception=None):
        if mensagem:
            super().__init__(mensagem)
        elif exception:
            super().__init__(exception)
        else:
            super().__init__()