class ClienteJaCadastradoException(Exception):
    """
    Exceção que representa um erro ao inserir um cliente no repositório.
    """

    def __init__(self):
        super().__init__("Cliente já cadastrado com esse CPF!")