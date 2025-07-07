class InicializacaoSistemaException(Exception):
    """
    Exceção que representa um erro na instância única do comunicador (erros no
    repositório).
    """

    def __init__(self):
        super().__init__("Não foi possível inicializar o sistema!")