class AcessoMenuClienteBloqueadoException(Exception):
    """
    Exceção que representa um erro ao tentar acessar o sistema relacionado ao
    cliente do banco.
    """

    def __init__(self):
        super().__init__("Número máximo de tentativas de acessar o sistema alcançado. Sistema encerrado!")