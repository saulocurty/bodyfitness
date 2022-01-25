from tkinter import *
from turtle import width
from tkinter import messagebox
from man_arquivos import *

class TelaMenu:
    def __init__(self, master=None):
        master.title("Menu")
        self.container1 = Frame(master, bg='red', width=600, height=200)
        self.container1["pady"] = 20
        self.container1["padx"] = 0
        self.container1.grid(column=0, row=0, pady=(40, 20))

        self.container2 = Frame(master, bg='blue', height=350, width=600)
        self.container2['pady'] = 20
        self.container2["padx"] = 10
        self.container2.grid(column=0, row=1)

        self.container3 = Frame(master)
        self.container3['pady'] = 20
        self.container3["padx"] = 10
        self.container3.grid(column=0, row=2)

        self.titulo =  Label(self.container1, text="MENU", font=("Arial", "20"))
        self.titulo.grid(column=0, row=0, padx=(250, 300))

        self.botao_add_a = Button(self.container2, text='Adicionar Alimento', width=12)
        self.botao_add_a.grid(column=0, row=0)

        self.botao_add_e = Button(self.container2, text='Adicionar Exercicio', width=12)
        self.botao_add_e.grid(column=2, row=0)

        self.botao_sel_a = Button(self.container2, text='Selecionar Alimento', width=12)
        self.botao_sel_a.grid(column=0, row=2)

        self.botao_sel_e = Button(self.container2, text='Selecionar Exercicio', width=12)
        self.botao_sel_e.grid(column=0, row=3)

        self.botao_rd = Button(self.container2, text='Resumo Diario', width=12)
        self.botao_rd.grid(column=0, row=4)









if __name__ == "__main__":     
    root = Tk()
    root.geometry("600x600") #tamanho da tela
    root.resizable(width=0, height=0)
    TelaMenu(root)
    root.mainloop()
