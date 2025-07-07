import tkinter as tk
from tkinter import messagebox, simpledialog

from src.negocio.Banco import Banco
from src.negocio.Cliente import Cliente

from src.exceptions.AtualizacaoNaoRealizadaException import AtualizacaoNaoRealizadaException
from src.exceptions.CampoVazioException import CampoVazioException
from src.exceptions.ClienteNaoCadastradoException import ClienteNaoCadastradoException
from src.exceptions.RepositorioException import RepositorioException

class AtualizarClienteFrame(tk.Tk):
    def __init__(self, banco: Banco, main_window):
        super().__init__()
        self.banco = banco
        self.main_window = main_window
        self.cliente: Cliente = None
        self.initialize()

    def initialize(self):
        self.title("Atualizar Cliente")
        self.geometry("400x300")
        self.resizable(False, False)

        cpf = simpledialog.askstring("CPF", "Informe o CPF do cliente:")

        if not cpf:
            self.destroy()
            return

        try:
            self.cliente = self.banco.procurar_cliente(cpf)
            if not self.cliente:
                raise ClienteNaoCadastradoException()
        except ClienteNaoCadastradoException:
            messagebox.showerror("Erro", "Cliente não cadastrado.")
            self.destroy()
            return

        # Widgets
        tk.Label(self, text="Dados do Cliente:").place(x=20, y=20)
        self.dados_cliente_text = tk.Text(self, wrap=tk.WORD, height=5, width=40, state=tk.DISABLED)
        self.dados_cliente_text.place(x=20, y=50)
        self.dados_cliente_text.configure(state=tk.NORMAL)
        self.dados_cliente_text.insert(tk.END, f"Dados:\n\n{self.cliente}")
        self.dados_cliente_text.configure(state=tk.DISABLED)

        tk.Label(self, text="Novo Nome:").place(x=20, y=160)
        self.novo_nome_entry = tk.Entry(self)
        self.novo_nome_entry.place(x=120, y=160, width=200)

        tk.Button(self, text="Atualizar", command=self.atualizar_cliente).place(x=60, y=220, width=100, height=40)
        tk.Button(self, text="Cancelar", command=self.cancelar).place(x=200, y=220, width=100, height=40)

    def atualizar_cliente(self):
        try:
            novo_nome = self.novo_nome_entry.get()
            self.verificar_campo_vazio(novo_nome, "Novo Nome")

            self.cliente.set_nome(novo_nome)
            self.banco.atualizar_cliente(self.cliente)

            messagebox.showinfo("Sucesso", "Cliente atualizado com sucesso!")
            self.novo_nome_entry.delete(0, tk.END)
            self.atualizar_dados_cliente_text()
        except CampoVazioException as e:
            messagebox.showwarning("Alerta", str(e))
        except (RepositorioException, AtualizacaoNaoRealizadaException) as e:
            messagebox.showerror(f"Erro {e}", str(e))

    def verificar_campo_vazio(self, campo, nome):
        if not campo:
            raise CampoVazioException(nome)

    def atualizar_dados_cliente_text(self):
        self.dados_cliente_text.configure(state=tk.NORMAL)
        self.dados_cliente_text.delete(1.0, tk.END)
        self.dados_cliente_text.insert(tk.END, f"Dados:\n\n{self.cliente}")
        self.dados_cliente_text.configure(state=tk.DISABLED)

    def cancelar(self):
        self.destroy()
        self.main_window.deiconify()

# # Exemplo de inicialização da aplicação
# if __name__ == "__main__":
#     from src.dados.RepositorioClientesArquivoDB import RepositorioClientesArquivoDB
#     from src.dados.RepositorioContasArquivoDB import RepositorioContasArquivoDB

#     banco = Banco(RepositorioClientesArquivoDB(), RepositorioContasArquivoDB())
#     app = AtualizarClienteFrame(banco, None)
#     app.mainloop()
