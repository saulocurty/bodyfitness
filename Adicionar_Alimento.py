from tkinter import *
from turtle import width
from man_arquivos import *
from tkinter import messagebox

class AdicionarAlimento:
    def __init__(self, master=None):
        master.title("Adicionar Alimento")
        self.user = Usuario('saulo', 19, 58, 'sullo152@gmail.com', 'm')
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



        self.titulo = Label(self.container1, text="Adicionar Alimento", font=("Arial", "16"))
        self.titulo.grid(column=0, row=0, padx=(20, 0))

        self.nomeAlimentoA = Label(self.container2, text="Nome", font=("Arial", "12"))
        self.nomeAlimentoA.grid(column=0, row=0, padx=(0,0), sticky='w')
        self.nomeAlimento = Entry(self.container2, width=10, font=("Arial", "12"))
        self.nomeAlimento.grid(column=1, row=0)

        self.caloriaAlimentoA = Label(self.container2, text="Calorias (100g)", font=("Arial", "12"))
        self.caloriaAlimentoA.grid(column=0, row=1, sticky='e')
        self.caloriaAlimento = Entry(self.container2, width=10, font=("Arial", "12"))
        self.caloriaAlimento.grid(column=1, row=1)

        self.botao1 = Button(self.container3, text="Adicionar Alimento", width=15)
        self.botao1['command'] = self.Adicionar
        self.botao1.grid(padx=(20, 0), pady=(30, 0))

    def Adicionar(self):
        comida = Alimento(
            self.nomeAlimento.get(),
            self.caloriaAlimento.get()
        )

        Inserir_Alimento('sullo152@gmail.com', comida)
        self.nomeAlimento.delete(0, 100)
        self.caloriaAlimento.delete(0, 100)

        



      
root = Tk()
root.geometry("300x300") #tamanho da tela
root.resizable(width=0, height=0)
AdicionarAlimento(root)
root.mainloop()