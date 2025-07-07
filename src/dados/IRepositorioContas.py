import sqlite3
from src.negocio.Conta import Conta
from src.negocio.ContaAbstrata import ContaAbstrata

from abc import ABC, abstractmethod

class IRepositorioContas(ABC):

    def inserir(self, conta: ContaAbstrata) -> bool:
        pass

    def procurar(self, numero: str) -> Conta:
        pass

    def remover(self, numero: str) -> bool:
        pass

    def atualizar(self, conta: ContaAbstrata) -> bool:
        pass

    def existe(self, numero: str) -> bool:
        pass

    def get_iterator(self):
        pass