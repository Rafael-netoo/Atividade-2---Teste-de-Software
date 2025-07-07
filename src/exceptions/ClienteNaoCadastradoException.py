class ClienteNaoCadastradoException(Exception):
    """
    Exceção que representa um erro quando uma busca de um cliente não cadastrado
    é feita.
    """

    def __init__(self):
        super().__init__("Nenhum cliente foi cadastrado com esse CPF!")