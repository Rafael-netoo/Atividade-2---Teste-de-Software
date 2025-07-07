import tkinter as tk
from tkinter import messagebox

from src.exceptions.CampoVazioException import CampoVazioException
from src.exceptions.ClienteJaPossuiContaException import ClienteJaPossuiContaException
from src.exceptions.ClienteNaoCadastradoException import ClienteNaoCadastradoException
from src.exceptions.ContaJaAssociadaException import ContaJaAssociadaException
from src.exceptions.ContaJaCadastradaException import ContaJaCadastradaException
from src.exceptions.RepositorioException import RepositorioException

from src.negocio.Banco import Banco
from src.negocio.Conta import Conta
from src.negocio.ContaImposto import ContaImposto
from src.negocio.ContaEspecial import ContaEspecial
from src.negocio.ContaPoupanca import ContaPoupanca


class AssociarContaFrame(tk.Tk):
    def __init__(self, banco: Banco, main_window):
        super().__init__()
        self.banco = banco
        self.main_window = main_window
        self.tipo_conta = Conta("", 0)
        self.initialize()

    def initialize(self):
        self.title("Associar Conta")
        self.geometry("400x300")
        self.resizable(False, False)

        # Widgets
        tk.Label(self, text="CPF:").place(x=20, y=20)
        self.cpf_cliente_entry = tk.Entry(self, width=30)
        self.cpf_cliente_entry.place(x=100, y=20)

        tk.Label(self, text="Nova Conta:").place(x=20, y=60)
        self.numero_conta_entry = tk.Entry(self, width=30)
        self.numero_conta_entry.place(x=100, y=60)

        tk.Label(self, text="Tipo da Conta:").place(x=20, y=100)

        self.tipo_conta_var = tk.StringVar(value="corrente")

        self.tipo_corrente_rb = tk.Radiobutton(
            self, text="Corrente", variable=self.tipo_conta_var, value="corrente", command=self.set_tipo_corrente
        )
        self.tipo_corrente_rb.place(x=50, y=130)

        self.tipo_poupanca_rb = tk.Radiobutton(
            self, text="Poupança", variable=self.tipo_conta_var, value="poupanca", command=self.set_tipo_poupanca
        )
        self.tipo_poupanca_rb.place(x=150, y=130)

        self.tipo_especial_rb = tk.Radiobutton(
            self, text="Especial", variable=self.tipo_conta_var, value="especial", command=self.set_tipo_especial
        )
        self.tipo_especial_rb.place(x=250, y=130)

        self.tipo_imposto_rb = tk.Radiobutton(
            self, text="Imposto", variable=self.tipo_conta_var, value="imposto", command=self.set_tipo_imposto
        )
        self.tipo_imposto_rb.place(x=330, y=130)

        tk.Button(self, text="Associar", command=self.associar_conta).place(x=85, y=200, width=100, height=40)
        tk.Button(self, text="Cancelar", command=self.cancelar).place(x=205, y=200, width=100, height=40)

    def set_tipo_corrente(self):
        self.tipo_conta = Conta("", 0)

    def set_tipo_poupanca(self):
        self.tipo_conta = ContaPoupanca("", 0)

    def set_tipo_especial(self):
        self.tipo_conta = ContaEspecial("", 0)

    def set_tipo_imposto(self):
        self.tipo_conta = ContaImposto("", 0)

    def associar_conta(self):
        try:
            cpf = self.cpf_cliente_entry.get()
            if not cpf:
                raise CampoVazioException("CPF")

            numero_conta = self.numero_conta_entry.get()
            if not numero_conta:
                raise CampoVazioException("Número da conta")

            self.tipo_conta.setNumero(numero_conta)
            self.tipo_conta.setSaldo(0)

            self.banco.cadastrar_conta(self.tipo_conta)
            self.banco.associar_conta(cpf, numero_conta)

            messagebox.showinfo("Sucesso", "Conta associada ao cliente com sucesso!")
            self.esvaziar_campos()
        except (
            ClienteNaoCadastradoException,
            ClienteJaPossuiContaException,
            ContaJaAssociadaException,
            ContaJaCadastradaException,
            RepositorioException
        ) as e:
            messagebox.showerror("Erro", str(e))
        except CampoVazioException as e:
            messagebox.showwarning("Alerta", str(e))

    def cancelar(self):
        self.esvaziar_campos()
        self.destroy()
        self.main_window.deiconify()

    def esvaziar_campos(self):
        self.cpf_cliente_entry.delete(0, tk.END)
        self.numero_conta_entry.delete(0, tk.END)
        self.tipo_corrente_rb.select()
        self.tipo_conta = Conta("", 0)

# # Exemplo de inicialização da aplicação
# if __name__ == "__main__":
#     from src.dados.RepositorioClientesArquivoDB import RepositorioClientesArquivoDB
#     from src.dados.RepositorioContasArquivoDB import RepositorioContasArquivoDB
#     banco = Banco(RepositorioClientesArquivoDB(), RepositorioContasArquivoDB())
#     app = AssociarContaFrame(banco, None)
#     app.mainloop()
