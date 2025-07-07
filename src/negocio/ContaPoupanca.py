
from src.negocio.Conta import Conta


class ContaPoupanca(Conta):

    def __init__(self, numero: str, saldo: float):
        super().__init__(numero, saldo)

    def render_juros(self, taxa: float) -> None:
        """
        Credita o valor dos juros à conta poupança com base na taxa fornecida.

        :param taxa: Taxa de juros a ser aplicada.
        """
        juros = self.getSaldo() * taxa
        self.creditar(juros)

    #METODO ADICIONAL
    def get_tipo(self) -> str:
        return "poupanca"
