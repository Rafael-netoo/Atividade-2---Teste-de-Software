from src.negocio.Conta import Conta

class ContaEspecial(Conta):
    """
    Conta bancária do tipo conta especial.
    """

    def __init__(self, numero: str, saldo: float):
        """
        Inicializa uma conta especial.

        :param numero: Número da conta.
        :param saldo: Saldo inicial da conta.
        """
        super().__init__(numero, saldo)
        self.__bonus = 0.0

    def getBonus(self) -> float:
        """
        Retorna o valor do bônus.
        """
        return self.__bonus
    
    def setBonus(self, bonus: float):
        """
        Define o valor do bônus.
        """
        self.__bonus = bonus

    def creditar(self, valor: float):
        """
        Credita um valor na conta e adiciona um bônus de 1% do valor creditado.

        :param valor: Valor a ser creditado na conta.
        """
        super().creditar(valor)
        self.__bonus += valor * 0.01

    def renderbonus(self):
        """
        Credita o valor acumulado de bônus na conta e reseta o bônus para zero.
        """
        super().creditar(self.__bonus)
        self.__bonus = 0.0

    #METODO ADICIONAL
    def get_tipo(self):
        return "especial"
