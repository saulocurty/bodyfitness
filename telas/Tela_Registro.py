from tkinter import *
from turtle import width


class TelaRegistro:
    def __init__(self, master=None):
        master.title("Regsitro")

        self.container1 = Frame(master)
        self.container1["pady"] = 20
        self.container1["padx"] = 50
        self.container1.grid(column=0, row=0, pady=(40, 0))

        self.container2 = Frame(master)
        self.container2['pady'] = 20
        self.container2["padx"] = 10
        self.container2.grid(column=0, row=1)

        self.container3 = Frame(master)
        #self.container3['pady'] = 20
        self.container3.grid(column=0, row=2)



        self.titulo = Label(self.container1, text="Registro", font=("Arial", "16"))
        self.titulo.grid(column=0, row=0, padx=(70, 0))

        self.nomeT = Label(self.container2, text="Nome", font=("Arial", "12"))
        self.nomeT.grid(column=0, row=0, padx=(0,0))
        self.nome = Entry(self.container2, width=10, font=("Arial", "12"))
        self.nome.grid(column=1, row=0)

        self.idadeT = Label(self.container2, text="Idade", font=("Arial", "12"))
        self.idadeT.grid(column=0, row=1)
        self.idade = Entry(self.container2, width=10, font=("Arial", "12"))
        self.idade.grid(column=1, row=1)

        self.alturaT = Label(self.container2, text="Altura", font=("Arial", "12"))
        self.alturaT.grid(column=0, row=2)
        self.altura = Entry(self.container2, width=10, font=("Arial", "12"))
        self.altura.grid(column=1, row=2)

        self.pesoT = Label(self.container2, text="Peso", font=("Arial", "12"))
        self.pesoT.grid(column=0, row=3)
        self.peso = Entry(self.container2, width=10, font=("Arial"))
        self.peso.grid(column=1, row=3)


        self.botao1 = Button(self.container3, text="Registro", width=10)
        self.botao1.grid(padx=(70, 0))






      
root = Tk()
root.geometry("300x300") #tamanho da tela
root.resizable(width=0, height=0)
TelaRegistro(root)
root.mainloop()