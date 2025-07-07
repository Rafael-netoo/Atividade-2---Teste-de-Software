from src.dados.RepositorioClientesArquivoDB import RepositorioClientesArquivoDB
from src.dados.RepositorioContasArquivoDB import RepositorioContasArquivoDB

from src.negocio.Banco import Banco

from src.gui.AtualizarClienteFrame import AtualizarClienteFrame
from src.gui.CadastrarClienteFrame import CadastrarClienteFrame
from src.gui.ClienteMenuFrame import ClienteMenuFrame
from src.gui.AssociarContaFrame import AssociarContaFrame
from src.gui.RemoverClienteFrame import RemoverClienteFrame
from src.gui.RemoverContaFrame import RemoverContaFrame

import tkinter as tk
banco = banco = Banco(RepositorioClientesArquivoDB(), RepositorioContasArquivoDB())

#cada janela vai ter um botão correspondente a ela

class MainInterface(tk.Tk):
    def __init__(self):
        super().__init__()
        self.initialize()

    def initialize(self):
        self.title("Banco")
        self.geometry("600x400")
        self.resizable(False, False)

        tk.Label(self, text="Escolha uma opção:").pack(pady=20)
        tk.Button(self, text="Cadastrar Cliente", command=self.cadastrar_cliente).pack(fill=tk.X, padx=20, pady=5)
        tk.Button(self, text="Atualizar Cliente", command=self.atualizar_cliente).pack(fill=tk.X, padx=20, pady=5)
        tk.Button(self, text="Menu Cliente", command=self.menu_cliente).pack(fill=tk.X, padx=20, pady=5)
        tk.Button(self, text="Associar Conta", command=self.associar_conta).pack(fill=tk.X, padx=20, pady=5)
        tk.Button(self, text="Remover Cliente", command=self.remover_cliente).pack(fill=tk.X, padx=20, pady=5)
        tk.Button(self, text="Remover Conta", command=self.remover_conta).pack(fill=tk.X, padx=20, pady=5)
        tk.Button(self, text="Sair", command=self.destroy).pack(fill=tk.X, padx=20, pady=5)

    def cadastrar_cliente(self):
        self.withdraw()
        new_window = CadastrarClienteFrame(banco, self)
        new_window.lift()
        new_window.protocol("WM_DELETE_WINDOW", lambda: self.quit())

    def atualizar_cliente(self):
        self.withdraw()
        new_window = AtualizarClienteFrame(banco, self)
        new_window.lift()
        new_window.protocol("WM_DELETE_WINDOW", lambda: self.quit())

    def menu_cliente(self):
        self.withdraw()
        new_window = ClienteMenuFrame(banco, self)
        new_window.lift()
        new_window.protocol("WM_DELETE_WINDOW", lambda: self.quit())
    
    def associar_conta(self):
        self.withdraw()
        new_window = AssociarContaFrame(banco, self)
        new_window.lift()
        new_window.protocol("WM_DELETE_WINDOW", lambda: self.quit())

    def remover_cliente(self):
        self.withdraw()
        new_window = RemoverClienteFrame(banco, self)
        new_window.lift()
        new_window.protocol("WM_DELETE_WINDOW", lambda: self.quit())

    def remover_conta(self):
        self.withdraw()
        new_window = RemoverContaFrame(banco, self)
        new_window.lift()
        new_window.protocol("WM_DELETE_WINDOW", lambda: self.quit())

    def on_close(self, new_window):
        new_window.destroy()
        self.deiconify()

if __name__ == "__main__":
    app = MainInterface()
    app.mainloop()
