import tkinter as tk
from tkinter import simpledialog, messagebox
from src.dados.RepositorioContasArquivoDB import RepositorioException
from src.exceptions import AtualizacaoNaoRealizadaException
from src.exceptions.CampoVazioException import CampoVazioException
from src.exceptions.ClienteNaoCadastradoException import ClienteNaoCadastradoException
from src.exceptions.ClienteNaoPossuiContaException import ClienteNaoPossuiContaException
from src.exceptions.ContaNaoEncontradaException import ContaNaoEncontradaException
from src.negocio.Banco import Banco


class RemoverContaFrame(tk.Toplevel):
    def __init__(self, banco: Banco, main_window):
        super().__init__()
        self.banco = banco
        self.main_window = main_window
        self.cliente = None
        self.initialize()

        try:
            cpf = simpledialog.askstring("CPF", "Informe o CPF do cliente:")
            if not cpf:
                return

            self.cliente = self.banco.procurar_cliente(cpf)
            if not self.cliente:
                raise CampoVazioException("Cliente não encontrado. Tente novamente.")

            if len(self.cliente.get_contas()) == 1:
                messagebox.showwarning("Alerta", "O cliente só possui 1 conta ativa. Remoção inválida.")
                self.cancelar()

        except ValueError as e:
            messagebox.showerror("Erro", str(e))
            return


    def initialize(self):
        self.title("Remover Conta")
        self.geometry("350x150")
        self.resizable(False, False)
        self.protocol("WM_DELETE_WINDOW", self.cancelar)

        # Labels e campos de texto
        self.numero_label = tk.Label(self, text="Número:")
        self.numero_label.place(x=20, y=20, width=70, height=20)

        self.numero_entry = tk.Entry(self)
        self.numero_entry.place(x=100, y=20, width=150, height=20)

        # Botão de Remover
        self.remover_button = tk.Button(self, text="Excluir", command=self.remover_conta)
        self.remover_button.place(x=60, y=60, width=100, height=40)

        # Botão de Cancelar
        self.cancelar_button = tk.Button(self, text="Cancelar", command=self.cancelar)
        self.cancelar_button.place(x=180, y=60, width=100, height=40)

    def remover_conta(self):
        try:
            numero_conta = self.numero_entry.get().strip()
            if not numero_conta:
                raise CampoVazioException("O campo Número está vazio.")

            if len(self.cliente.get_contas()) == 1:
                raise ValueError("O cliente só possui 1 conta ativa. Remoção inválida.")

            self.banco.remover_conta(self.cliente, numero_conta)

            messagebox.showinfo("Sucesso", "Conta removida com sucesso!")
            self.esvaziar_campos()

        except (RepositorioException or ContaNaoEncontradaException or 
                ClienteNaoPossuiContaException or AtualizacaoNaoRealizadaException 
                or ClienteNaoCadastradoException) as e:
            messagebox.showwarning("Alerta", str(e))
        except Exception as e:
            messagebox.showerror("Erro", str(e))
            self.esvaziar_campos()

    def esvaziar_campos(self):
        self.numero_entry.delete(0, tk.END)

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
#     app = RemoverContaFrame(banco, main_window)
#     app.mainloop()