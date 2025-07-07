import tkinter as tk
from tkinter import simpledialog, messagebox

from src.exceptions.ClienteNaoPossuiContaException import ClienteNaoPossuiContaException
from src.exceptions.ContaNaoEncontradaException import ContaNaoEncontradaException
from src.exceptions.ContasOrigemDestinoIguaisException import ContasOrigemDestinoIguaisException
from src.exceptions.EntradaInvalidaException import EntradaInvalidaException
from src.exceptions.SaldoInsuficienteException import SaldoInsuficienteException
from src.exceptions.ValorInvalidoException import ValorInvalidoException

from src.negocio.Banco import Banco
from src.negocio.ContaAbstrata import ContaAbstrata


class ClienteMenuFrame(tk.Tk):
    def __init__(self, banco: Banco, main_window):
        super().__init__()
        self.banco = banco
        self.main_window = main_window
        self.cliente = None
        self.initialize()

    def initialize(self):
        self.title("Menu Cliente")
        self.geometry("400x300")
        self.resizable(False, False)

        while True:
            cpf = simpledialog.askstring("CPF", "Informe o CPF do cliente:")
            if not cpf:
                self.destroy()
                return

            self.cliente = self.banco.procurar_cliente(cpf)
            if self.cliente:
                break
            else:
                messagebox.showerror("Erro", "Cliente não encontrado. Tente novamente.")

        tk.Label(self, text=f"Bem-vindo, {self.cliente.nome}!").pack(pady=10)

        tk.Button(self, text="Consultar Saldo", command=self.consultar_saldo).pack(fill=tk.X, padx=20, pady=5)
        tk.Button(self, text="Depositar", command=self.depositar).pack(fill=tk.X, padx=20, pady=5)
        tk.Button(self, text="Sacar", command=self.sacar).pack(fill=tk.X, padx=20, pady=5)
        tk.Button(self, text="Transferir", command=self.transferir).pack(fill=tk.X, padx=20, pady=5)
        tk.Button(self, text="Sair", command=self.cancelar).pack(fill=tk.X, padx=20, pady=5)

    def consultar_saldo(self):
        try:
            numero_conta = simpledialog.askstring("Conta", "Informe o número da conta:")
            if not numero_conta:
                return

            conta: ContaAbstrata = self.buscar_conta_cliente(numero_conta)
            messagebox.showinfo("Saldo", f"Saldo: R${conta.getSaldo():.2f}")
        except ClienteNaoPossuiContaException as e:
            messagebox.showwarning("Aviso", str(e))

    def depositar(self):
        try:
            numero_conta = simpledialog.askstring("Conta", "Informe o número da conta:")
            if not numero_conta:
                return

            valor = simpledialog.askfloat("Depositar", "Informe o valor a ser depositado:")
            if valor is None:
                return

            conta = self.buscar_conta_cliente(numero_conta)
            self.banco.creditar(conta, valor)
            conta.setSaldo(conta.getSaldo() + valor)

            messagebox.showinfo("Sucesso", "Depósito realizado com sucesso!")
        except (ClienteNaoPossuiContaException, EntradaInvalidaException, ValorInvalidoException) as e:
            messagebox.showerror("Erro", str(e))

    def sacar(self):
        try:
            numero_conta = simpledialog.askstring("Conta", "Informe o número da conta:")
            if not numero_conta:
                return

            valor = simpledialog.askfloat("Saque", "Informe o valor a ser sacado:")
            if valor is None:
                return

            conta = self.buscar_conta_cliente(numero_conta)
            self.banco.debitar(conta, valor)

            messagebox.showinfo("Sucesso", "Saque realizado com sucesso!")
        except (ClienteNaoPossuiContaException, EntradaInvalidaException, SaldoInsuficienteException) as e:
            messagebox.showerror("Erro", str(e))

    def transferir(self):
        try:
            conta_origem = simpledialog.askstring("Conta Origem", "Informe o número da conta de origem:")
            if not conta_origem:
                return

            conta_destino = simpledialog.askstring("Conta Destino", "Informe o número da conta de destino:")
            if not conta_destino:
                return

            if conta_origem == conta_destino:
                raise ContasOrigemDestinoIguaisException("As contas de origem e destino devem ser diferentes.")

            valor = simpledialog.askfloat("Transferência", "Informe o valor da transferência:")
            if valor is None:
                return

            conta_origem_obj = self.buscar_conta_cliente(conta_origem)
            conta_destino_obj = self.banco.procurar_conta(conta_destino)
            if not conta_destino_obj:
                raise ContaNaoEncontradaException()

            self.banco.transferir(conta_origem_obj, conta_destino_obj, valor)

            messagebox.showinfo("Sucesso", "Transferência realizada com sucesso!")
        except (ClienteNaoPossuiContaException, ContaNaoEncontradaException,
                ContasOrigemDestinoIguaisException, EntradaInvalidaException,
                SaldoInsuficienteException, ValorInvalidoException) as e:
            messagebox.showerror("Erro", str(e))

    def buscar_conta_cliente(self, numero_conta: str):
        conta = self.banco.procurar_conta(numero_conta)
        if not conta or numero_conta not in [c for c in self.cliente.contas]:
            raise ClienteNaoPossuiContaException()
        return conta
    
    def cancelar(self):
        self.destroy()
        self.main_window.deiconify()

# # Exemplo de inicialização da aplicação
# if __name__ == "__main__":
#     from src.dados.RepositorioClientesArquivoDB import RepositorioClientesArquivoDB
#     from src.dados.RepositorioContasArquivoDB import RepositorioContasArquivoDB

#     banco = Banco(RepositorioClientesArquivoDB(), RepositorioContasArquivoDB())
#     app = ClienteMenuFrame(banco, None)
#     app.mainloop()