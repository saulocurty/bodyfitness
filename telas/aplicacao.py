from tkinter import *


class Aplicacao:

    def __init__(self, master=None):
        self.fonte = ("Arial", "10")
        self.primeiroContainer = Frame(master,borderwidth = 3, relief="sunken")
        self.primeiroContainer["pady"] = 10
        self.primeiroContainer.pack()

        self.segundoContainer = Frame(master)
        self.segundoContainer["padx"] = 20
        self.segundoContainer.pack()

        self.terceiroContainer = Frame(master)
        self.terceiroContainer["padx"] = 20
        self.terceiroContainer.pack()

        self.quartoContainer = Frame(master)
        self.quartoContainer["padx"] = 20
        self.quartoContainer.pack()

        self.titulo = Label(self.primeiroContainer, text="Dados do usuario", font=self.fonte)
        self.titulo.pack()

        self.nomeLabel = Label(self.segundoContainer, text="Nome", font=self.fonte)
        self.nomeLabel.pack(side=LEFT)
        self.nome = Entry(self.segundoContainer)
        self.nome["width"] = 30
        self.nome["font"] = self.fonte
        self.nome.pack(side=LEFT)

        self.senhaLabel = Label(self.terceiroContainer, text="Senha", font=self.fonte)
        self.senhaLabel.pack(side=LEFT)
        
        self.senha=Entry(self.terceiroContainer, width=30, font=self.fonte,show="*")
        self.senha.pack(side=LEFT)

root = Tk()

Aplicacao(root)
root.mainloop()

