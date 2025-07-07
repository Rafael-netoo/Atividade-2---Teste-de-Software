from typing import List

from src.exceptions.ClienteJaPossuiContaException import ClienteJaPossuiContaException
from src.exceptions.ClienteNaoPossuiContaException import ClienteNaoPossuiContaException


class Cliente:

    def __init__(self, nome: str, cpf: str):
        """
        Inicializa o cliente com nome e CPF.
        
        :param nome: Nome do cliente.
        :param cpf: CPF do cliente.
        """
        self.nome = nome
        self.cpf = cpf
        self.contas: List[str] = []

    def get_nome(self) -> str:
        return self.nome

    def set_nome(self, nome: str):
        self.nome = nome

    def get_cpf(self) -> str:
        return self.cpf

    def set_cpf(self, cpf: str):
        self.cpf = cpf

    def get_contas(self) -> List[str]:
        return self.contas

    def adicionar_conta(self, numero_conta: str):
        """
        Adiciona um número de conta ao cliente.

        :param numero_conta: Número da conta a ser adicionada.
        :raises ClienteJaPossuiContaException: Se o cliente já tiver a conta.
        """
        if self.procurar_conta(numero_conta) != -1:
            raise ClienteJaPossuiContaException()
        self.contas.append(numero_conta)

    def remover_conta(self, numero_conta: str):
        """
        Remove um número de conta associado ao cliente.

        :param numero_conta: Número da conta a ser removida.
        :raises ClienteNaoPossuiContaException: Se o cliente não tiver a conta.
        """
        index = self.procurar_conta(numero_conta)
        if index == -1:
            raise ClienteNaoPossuiContaException()
        self.contas.pop(index)

    def remover_todas_as_contas(self):
        """Remove todas as contas associadas ao cliente."""
        self.contas.clear()

    def procurar_conta(self, numero_conta: str) -> int:
        """
        Busca um número de conta nas contas do cliente.

        :param numero_conta: Número da conta a ser procurada.
        :return: O índice da conta ou -1 se não encontrada.
        """
        try:
            return self.contas.index(numero_conta)
        except ValueError:
            return -1

    def consultar_numero_conta(self, i: int) -> str:
        """
        Retorna o número da conta em uma posição específica.

        :param i: Índice da conta.
        :return: Número da conta.
        """
        return self.contas[i]

    def __eq__(self, other) -> bool:
        if isinstance(other, Cliente):
            return other.get_cpf() == self.cpf
        return False

    def __str__(self) -> str:
        return f"Nome: {self.nome}\nCPF: {self.cpf}\nContas: {self.contas}"