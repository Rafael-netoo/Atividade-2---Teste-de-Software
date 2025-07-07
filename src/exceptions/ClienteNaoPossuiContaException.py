class ClienteNaoPossuiContaException(Exception):
    """
    Exceção que representa um erro ao buscar uma conta não inserida no banco de
    dados.
    """

    def __init__(self):
        super().__init__("O cliente não possui conta com este número!")