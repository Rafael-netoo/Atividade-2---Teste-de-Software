from abc import ABC, abstractmethod
from src.negocio import ContaAbstrata

class IteratorContaAbstrata(ABC):

    @abstractmethod
    def has_next(self) -> bool:
        """
        Indica a existência de uma conta.

        :return: Se a conta foi encontrada. Retorna False se for None ou o fim do array.
        """
        pass

    @abstractmethod
    def next(self) -> ContaAbstrata:
        """
        Retorna uma conta da posição atual no array.

        :return: A conta encontrada ou None se não houver mais contas no array.
        """
        pass