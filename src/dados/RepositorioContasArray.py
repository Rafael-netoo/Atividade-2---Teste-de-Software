from src.dados.IRepositorioContas import IRepositorioContas
from src.negocio.ContaAbstrata import ContaAbstrata

class RepositorioContasArray(IRepositorioContas):
    def __init__(self):
        """
        Constrói um repositório com array.
        Tamanho inicial do array são 100 posições.
        """
        self.__contas = [None] * 100
        self.indice = 0

    def __get_indice(self, numero: str) -> int:
        """
        Retorna o índice da conta no array.
        :param numero: Número da conta cujo índice é retornado.
        :return: Índice da conta no array. Igual a self.indice caso a conta não exista.
        """
        for i in range(self.indice):
            if self.__contas[i].getNumero() == numero:
                return i
        return self.indice

    def inserir(self, conta: ContaAbstrata) -> bool:
        """
        Insere uma nova conta no array.
        :param conta: Objeto do tipo ContaAbstrata.
        :return: True se inserido com sucesso, False se a conta já existir.
        """
        if self.existe(conta.getNumero()):
            return False
        if self.indice == len(self.__contas):
            self.__contas.extend([None] * len(self.__contas))
        self.__contas[self.indice] = conta
        self.indice += 1
        return True

    def procurar(self, numero: str) -> ContaAbstrata:
        """
        Procura uma conta pelo número.
        :param numero: Número da conta.
        :return: Um objeto do tipo ContaAbstrata ou None se não encontrado.
        """
        i = self.__get_indice(numero)
        if i < self.indice:
            return self.__contas[i]
        return None

    def remover(self, numero: str) -> bool:
        """
        Remove uma conta pelo número.
        :param numero: Número da conta.
        :return: True se removido com sucesso, False se a conta não existir.
        """
        i = self.__get_indice(numero)
        if i < self.indice:
            self.indice -= 1
            self.__contas[i] = self.__contas[self.indice]
            self.__contas[self.indice] = None
            return True
        return False

    def atualizar(self, conta: ContaAbstrata) -> bool:
        """
        Atualiza as informações de uma conta.
        :param conta: Objeto do tipo ContaAbstrata.
        :return: True se atualizado com sucesso, False se a conta não existir.
        """
        i = self.__get_indice(conta.getNumero())
        if i < self.indice:
            self.__contas[i] = conta
            return True
        return False

    def existe(self, numero: str) -> bool:
        """
        Verifica se uma conta existe pelo número.
        :param numero: Número da conta.
        :return: True se a conta existir, False caso contrário.
        """
        return self.__get_indice(numero) != self.indice

    def get_iterator(self):
        """
        Retorna um iterador para percorrer as contas no array.
        :return: Iterador para contas.
        """
        return (conta for conta in self.__contas if conta is not None)
