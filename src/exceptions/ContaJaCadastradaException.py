class ContaJaCadastradaException(Exception):
    """
    Exceção que representa um erro caso o sistema tente cadastrar os dados de um
    cliente já cadastrado.
    """

    def __init__(self):
        super().__init__("Já existe uma conta cadastrada com este número!")