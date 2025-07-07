class RemocaoInvalidaException(Exception):
    """
    Exceção que representa um erro na remoção de uma conta de um cliente que só
    possui a própria conta a ser removida como única conta.
    """

    def __init__(self):
        super().__init__("A remoção não pode ser concluída! O cliente só possui esta conta!")