from tkinter import *
from turtle import width
from telas.man_arquivos import *
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



        self.titulo = Label(self.container1, text="Adicionar Exercicio", font=("Arial", "16"))
        self.titulo.grid(column=0, row=0, padx=(20, 0))

        self.nomeExercicioA = Label(self.container2, text="Nome", font=("Arial", "12"))
        self.nomeExercicioA.grid(column=0, row=0, padx=(0,0), sticky='w')
        self.nomeExercicio = Entry(self.container2, width=10, font=("Arial", "12"))
        self.nomeExercicio.grid(column=1, row=0)

        self.caloriaExercicioA = Label(self.container2, text="Calorias Homem", font=("Arial", "12"))
        self.caloriaExercicioA.grid(column=0, row=1, sticky='e')
        self.caloriaExercicio = Entry(self.container2, width=10, font=("Arial", "12"))
        self.caloriaExercicio.grid(column=1, row=1)

        self.cloriaExercicioM = Label(self.container2, text="Calorias Mulher", font=("Arial", "12"))
        self.caloriaExercicioMu = Entry(self.container2, width=10, font=("Arial", "12"))
        self.caloriaExercicioMu.grid(row=2, column=1)
        self.cloriaExercicioM.grid(column=0, row=2, sticky='w')


        self.botao1 = Button(self.container3, text="Adicionar Alimento", width=15)
        self.botao1['command'] = self.Adicionar
        self.botao1.grid(padx=(20, 0), pady=(30, 0))

    def Adicionar(self):
        exercicio = Exercicio(
            self.nomeExercicio.get(),
            self.caloriaExercicio.get(),
            self.caloriaExercicioMu.get()
        )

        Inserir_Exercicio('sullo152@gmail.com', exercicio)

        self.nomeExercicio.delete(0, 100)
        self.caloriaExercicio.delete(0, 100)
        self.caloriaExercicioMu.delete(0, 100)


        def Proseguir():
            pass
      
root = Tk()
root.geometry("300x300") #tamanho da tela
root.resizable(width=0, height=0)
AdicionarAlimento(root)
root.mainloop()