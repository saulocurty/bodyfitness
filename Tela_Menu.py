from tkinter import *
from tkinter import ttk
from turtle import width
from tkinter import messagebox
from man_arquivos import *

class TelaMenu:
    def __init__(self, master=None):
        master.title("Menu")
        self.container1 = Frame(master, width=600, height=200)
        self.container1["pady"] = 20
        self.container1["padx"] = 0
        self.container1.grid(column=0, row=0, pady=(40, 0))

        self.container2 = Frame(master)
        #self.container2['pady'] = 20
        #self.container2["padx"] = 10
        self.container2.grid(column=0, row=1, padx=(35, 0))

        self.container3 = Frame(master)
        #self.container3['pady'] = 20
        #self.container3["padx"] = 10
        self.container3.grid(column=0, row=2)

        self.titulo =  Label(self.container1, text="MENU", font=("Arial", "20", 'bold'))
        self.titulo.grid(column=0, row=0, padx=(50, 0))

        self.botao_add_a = Button(self.container2, text='Adicionar Alimento', width=15)
        self.botao_add_a.grid(column=0, row=0, padx=(0, 5), pady=(0, 10))

        self.botao_add_e = Button(self.container2, text='Adicionar Exercicio', width=15)
        self.botao_add_e.grid(column=1, row=0,  pady=(0, 10))

        self.botao_sel_a = Button(self.container2, text='Selecionar Alimento', width=15)
        self.botao_sel_a.grid(column=0, row=2,padx=(0, 5), pady=(0, 10))

        self.botao_sel_e = Button(self.container2, text='Selecionar Exercicio', width=15)
        self.botao_sel_e.grid(column=1, row=2, pady=(0, 10))

        self.botao_rd = Button(self.container3, text='Resumo Diario', width=15, bg='red')
        self.botao_rd.grid(column=0, row=4, pady=(30, 0), padx=(30, 0))









if __name__ == "__main__":     
    root = Tk()
    root.geometry("300x300") #tamanho da tela
    root.resizable(width=0, height=0)
    TelaMenu(root)
    root.mainloop()
