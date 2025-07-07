from abc import ABC, abstractmethod
from src.negocio import Cliente

class IteratorCliente(ABC):

    @abstractmethod
    def has_next(self) -> bool:
        """
        Indica a existência de um cliente.

        :return: Se o cliente foi encontrado. Retorna False se for None ou o fim do array.
        """
        pass

    @abstractmethod
    def next(self) -> Cliente:
        """
        Retorna um cliente da posição atual no array.

        :return: O cliente encontrado ou None se não houver mais clientes no array.
        """
        pass
