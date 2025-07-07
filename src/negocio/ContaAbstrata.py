from abc import ABC, abstractmethod
from src.exceptions import SaldoInsuficienteException

class ContaAbstrata(ABC):
    """
    Classe abstrata de uma conta bancária.
    """

    def __init__(self, numero: str, saldo: float):
        """
        Inicializa uma conta bancária.

        :param numero: Número da conta.
        :param saldo: Valor do saldo inicial da conta.
        """
        self.__numero = numero
        self.__saldo = saldo

    def getNumero(self) -> str:
        """
        Retorna o número da conta.
        """
        return self.__numero

    
    def setNumero(self, numero: str):
        """
        Define o número da conta.
        """
        self.__numero = numero

    
    def getSaldo(self) -> float:
        """
        Retorna o saldo da conta.
        """
        return self.__saldo

    def setSaldo(self, saldo: float):
        """
        Define o saldo da conta.
        """
        self.__saldo = saldo

    def creditar(self, valor: float):
        """
        Credita um valor na conta bancária.

        :param valor: Valor a ser creditado na conta.
        """
        if valor > 0:
            self.__saldo += valor

    @abstractmethod
    def debitar(self, valor: float):
        """
        Debita um valor da conta bancária.

        :param valor: Valor a ser debitado da conta.
        :raises SaldoInsuficienteException: Se o valor exceder o saldo disponível.
        """
        pass

    #METODO ADICIONAL
    @abstractmethod
    def get_tipo(self) -> str:
        """
        Retorna o tipo da conta.
        """
        pass

    def __eq__(self, other):
        """
        Verifica se duas contas são iguais com base no número da conta.
        """
        if isinstance(other, ContaAbstrata):
            return self.__numero == other.__numero
        return False