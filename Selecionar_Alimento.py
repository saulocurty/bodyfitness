from tkinter import *
from tkinter import ttk
from man_arquivos import *


class SelecionarExercicio:
    def __init__(self, master=None):
        master.title("Selecionar Alimento")
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

        self.comboAlimento = ttk.Combobox(
            self.container2,
            
        )


root = Tk()
root.geometry("300x300") #tamanho da tela
root.resizable(width=0, height=0)
SelecionarExercicio(root)
root.mainloop()