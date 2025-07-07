import tkinter as tk
from tkinter import messagebox

from src.negocio.Banco import Banco


class RemoverClienteFrame(tk.Toplevel):
    instance_remover_cliente_frame = None

    def __init__(self, banco: Banco, main_window):
        super().__init__()
        self.main_window = main_window
        self.banco = banco
        self.title("Remover Cliente")
        self.geometry("350x150")
        self.resizable(False, False)
        self.protocol("WM_DELETE_WINDOW", self.cancelar)

        self.cpf_label = tk.Label(self, text="CPF:")
        self.cpf_label.place(x=20, y=20, width=50, height=20)

        self.cpf_entry = tk.Entry(self)
        self.cpf_entry.place(x=100, y=20, width=150, height=20)

        self.remover_button = tk.Button(
            self, text="Excluir", command=self.remover_cliente)
        self.remover_button.place(x=65, y=60, width=100, height=40)

        self.cancelar_button = tk.Button(
            self, text="Cancelar", command=self.cancelar)
        self.cancelar_button.place(x=185, y=60, width=100, height=40)

    @classmethod
    def get_instance(cls, main_window):
        if cls.instance_remover_cliente_frame is None:
            cls.instance_remover_cliente_frame = RemoverClienteFrame(main_window)
        return cls.instance_remover_cliente_frame

    def remover_cliente(self):
        try:
            cpf = self.cpf_entry.get().strip()
            if not cpf:
                raise ValueError("O campo CPF está vazio.")

            cliente = self.banco.procurar_cliente(cpf)
            if cliente is None:
                raise ValueError("Cliente não cadastrado.")

            self.banco.remover_cliente(cpf)

            messagebox.showinfo(
                "Sucesso",
                "Cliente removido com sucesso! Todas as contas associadas a ele também foram removidas!"
            )
            self.esvaziar_campos()
        except ValueError as e:
            messagebox.showwarning("Alerta", str(e))
        except Exception as e:
            messagebox.showerror("Erro", str(e))
            self.esvaziar_campos()

    def esvaziar_campos(self):
        self.cpf_entry.delete(0, tk.END)

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
#     app = RemoverClienteFrame(banco, main_window)
#     app.mainloop()