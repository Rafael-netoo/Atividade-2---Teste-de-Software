import sqlite3
from src.dados.IRepositorioContas import IRepositorioContas
from src.exceptions.RepositorioException import RepositorioException
from src.negocio.ContaImposto import ContaImposto
from src.negocio.Conta import Conta
from src.negocio.ContaAbstrata import ContaAbstrata
from src.negocio.ContaEspecial import ContaEspecial
from src.negocio.ContaPoupanca import ContaPoupanca


class RepositorioContasArquivoDB(IRepositorioContas):
    def __init__(self, db_path="contas.db"):
        """
        Inicializa o repositório, conectando-se ao banco de dados SQLite.
        Cria a tabela de contas se ela não existir.
        """
        self.db_path = db_path
        try:
            with self._connect() as conn:
                cursor = conn.cursor()
                cursor.execute("""
                    CREATE TABLE IF NOT EXISTS contas (
                        numero TEXT PRIMARY KEY,
                        saldo REAL NOT NULL,
                        tipo TEXT NOT NULL
                    )
                """)
        except Exception as e:
            raise RepositorioException("Erro ao inicializar o banco de dados.", e)

    def _connect(self):
        """
        Cria uma conexão com o banco de dados.
        """
        try:
            return sqlite3.connect(self.db_path)
        except Exception as e:
            raise RepositorioException("Erro ao conectar ao banco de dados.", e)

    def inserir(self, conta: ContaAbstrata) -> bool:
        """
        Insere uma nova conta no banco de dados.
        :param conta: Dicionário contendo 'numero', 'saldo'.
        :return: True se inserido com sucesso, False se ocorrer erro.
        """
        try:
            with self._connect() as conn:
                cursor = conn.cursor()
                cursor.execute("""
                    INSERT INTO contas (numero, saldo, tipo)
                    VALUES (?, ?, ?)
                """, (conta.getNumero(), conta.getSaldo(), conta.get_tipo()))
                conn.commit()
            return True
        except Exception as e:
            raise RepositorioException(f"Erro ao inserir conta no banco de dados. {e}", e)

    def procurar(self, numero: str) -> ContaAbstrata:
        """
        Procura uma conta pelo número.
        :param numero: Número da conta.
        :return: Um objeto do tipo ContaAbstrata.
        """
        try:
            with self._connect() as conn:
                cursor = conn.cursor()
                cursor.execute("SELECT * FROM contas WHERE numero = ?", (numero,))
                row = cursor.fetchone()
                if row:
                    if row[2] == 'conta':
                        return Conta(row[0], row[1])
                    elif row[2] == 'especial':
                        return ContaEspecial(row[0], row[1])
                    elif row[2] == 'poupanca':
                        return ContaPoupanca(row[0], row[1])
                    elif row[2] == 'imposto':
                        return ContaImposto(row[0], row[1])
                    else:
                        return Conta(row[0], row[1])
                return None
        except Exception as e:
            raise RepositorioException("Erro ao procurar conta no banco de dados.", e)

    def remover(self, numero: str) -> bool:
        """
        Remove uma conta pelo número.
        :param numero: Número da conta.
        :return: True se removido com sucesso, False se ocorrer erro.
        """
        try:
            with self._connect() as conn:
                cursor = conn.cursor()
                cursor.execute("DELETE FROM contas WHERE numero = ?", (numero,))
                conn.commit()
            return True
        except Exception as e:
            raise RepositorioException("Erro ao remover conta do banco de dados.", e)

    def atualizar(self, conta: ContaAbstrata) -> bool:
        """
        Atualiza as informações de uma conta.
        :param conta: Dicionário contendo 'numero', 'saldo'.
        :return: True se atualizado com sucesso, False se ocorrer erro.
        """
        try:
            with self._connect() as conn:
                cursor = conn.cursor()
                cursor.execute("""
                    UPDATE contas SET  saldo = ? WHERE numero = ?
                """, (conta.getSaldo(), conta.getNumero()))
                conn.commit()
            return True
        except Exception as e:
            raise RepositorioException("Erro ao atualizar conta no banco de dados.", e)

    def existe(self, numero: str) -> bool:
        """
        Verifica se uma conta existe pelo número.
        :param numero: Número da conta.
        :return: True se a conta existir, False caso contrário.
        """
        try:
            with self._connect() as conn:
                cursor = conn.cursor()
                cursor.execute("SELECT 1 FROM contas WHERE numero = ?", (numero,))
                row = cursor.fetchone()
                return row is not None
        except Exception as e:
            raise RepositorioException("Erro ao verificar existência de conta no banco de dados.", e)

    def get_iterator(self):
        """
        Retorna um iterador para percorrer as contas no banco de dados.
        :return: Iterador para contas.
        """
        try:
            with self._connect() as conn:
                cursor = conn.cursor()
                cursor.execute("SELECT * FROM contas")
                rows = cursor.fetchall()
                for row in rows:
                    yield {'numero': row[0], 'saldo': row[1]}
        except Exception as e:
            raise RepositorioException("Erro ao obter iterador de contas do banco de dados.", e)
