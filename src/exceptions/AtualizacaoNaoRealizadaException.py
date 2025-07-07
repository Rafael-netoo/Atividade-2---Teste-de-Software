class AtualizacaoNaoRealizadaException(Exception):
    """
    Exceção que representa um erro na atualização de dados do cliente.
    """

    def __init__(self):
        super().__init__("Atualização não realizada! Erro no repositório!")