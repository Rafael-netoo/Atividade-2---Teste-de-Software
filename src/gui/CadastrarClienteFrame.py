import tkinter as tk
from tkinter import messagebox

from src.negocio.Banco import Banco
from src.negocio.ContaImposto import ContaImposto
from src.negocio.Cliente import Cliente
from src.negocio.Conta import Conta
from src.negocio.ContaEspecial import ContaEspecial
from src.negocio.ContaPoupanca import ContaPoupanca

from src.exceptions.CampoVazioException import CampoVazioException
from src.exceptions.ClienteJaCadastradoException import ClienteJaCadastradoException
from src.exceptions.ContaJaCadastradaException import ContaJaCadastradaException

class CadastrarClienteFrame(tk.Toplevel):
    def __init__(self, banco: Banco, main_window):
        super().__init__()
        self.banco = banco
        self.main_window = main_window
        self.tipo_conta = Conta("", 0)
        self.tipo_conta_var = tk.StringVar(value="Corrente")
        self.initialize()

    def initialize(self):
        self.title("Cadastrar")
        self.geometry("400x300")
        self.resizable(False, False)

        # Widgets
        tk.Label(self, text="CPF:").place(x=20, y=20)
        self.cpf_entry = tk.Entry(self)
        self.cpf_entry.place(x=130, y=20, width=100)

        tk.Label(self, text="Nome:").place(x=20, y=55)
        self.nome_entry = tk.Entry(self)
        self.nome_entry.place(x=130, y=55, width=130)

        tk.Label(self, text="Numero da conta:").place(x=20, y=90)
        self.conta_entry = tk.Entry(self)
        self.conta_entry.place(x=130, y=90, width=100)

        tk.Label(self, text="Tipo da Conta:").place(x=20, y=120)

        tk.Radiobutton(self, text="Corrente", variable=self.tipo_conta_var, value="Corrente", command=self.set_conta_corrente).place(x=50, y=150)
        tk.Radiobutton(self, text="ContaPoupanca", variable=self.tipo_conta_var, value="ContaPoupanca", command=self.set_conta_poupanca).place(x=140, y=150)
        tk.Radiobutton(self, text="Especial", variable=self.tipo_conta_var, value="Especial", command=self.set_conta_especial).place(x=229, y=150)
        tk.Radiobutton(self, text="Imposto", variable=self.tipo_conta_var, value="Imposto", command=self.set_conta_imposto).place(x=310, y=150)

        tk.Button(self, text="Cadastrar", command=self.submeter_cadastro).place(x=35, y=200, width=100, height=40)
        tk.Button(self, text="Desfazer", command=self.esvaziar_campos).place(x=147, y=200, width=100, height=40)
        tk.Button(self, text="Cancelar", command=self.cancelar).place(x=260, y=200, width=100, height=40)

    def set_conta_corrente(self):
        self.tipo_conta = Conta("", 0)

    def set_conta_poupanca(self):
        self.tipo_conta = ContaPoupanca("", 0)

    def set_conta_especial(self):
        self.tipo_conta = ContaEspecial("", 0)

    def set_conta_imposto(self):
        self.tipo_conta = ContaImposto("", 0)

    def submeter_cadastro(self):
        try:
            cpf = self.cpf_entry.get()
            self.verificar_campo_vazio(cpf, "CPF")

            nome = self.nome_entry.get()
            self.verificar_campo_vazio(nome, "Nome")

            numero_conta = self.conta_entry.get()
            self.verificar_campo_vazio(numero_conta, "Numero da Conta")

            if self.banco.procurar_cliente(cpf):
                raise ClienteJaCadastradoException()
            if self.banco.procurar_conta(numero_conta):
                raise ContaJaCadastradaException()

            self.tipo_conta.setNumero(numero_conta)
            self.tipo_conta.setSaldo(0)

            cliente = Cliente(nome, cpf)
            cliente.adicionar_conta(numero_conta)

            self.banco.cadastrar_conta(self.tipo_conta)
            self.banco.cadastrar_cliente(cliente)

            messagebox.showinfo("Sucesso", "Cliente cadastrado com sucesso!")
            self.esvaziar_campos()

        except (Exception) as e:
            messagebox.showerror("Erro", str(e))
        except CampoVazioException as e:
            messagebox.showwarning("Alerta", str(e))

    def verificar_campo_vazio(self, campo, nome):
        if not campo:
            raise CampoVazioException(nome)

    def esvaziar_campos(self):
        self.cpf_entry.delete(0, tk.END)
        self.nome_entry.delete(0, tk.END)
        self.conta_entry.delete(0, tk.END)
        self.tipo_conta_var.set("Corrente")
        self.set_conta_corrente()

    def cancelar(self):
        self.esvaziar_campos()
        self.destroy()
        self.main_window.deiconify()

# # Exemplo de inicialização da aplicação
# if __name__ == "__main__":
#     from src.dados.RepositorioClientesArquivoDB import RepositorioClientesArquivoDB
#     from src.dados.RepositorioContasArquivoDB import RepositorioContasArquivoDB

#     banco = Banco(RepositorioClientesArquivoDB(), RepositorioContasArquivoDB())
#     main_window = tk.Tk()
#     main_window.withdraw()
#     app = CadastrarClienteFrame(banco, main_window)
#     app.mainloop()