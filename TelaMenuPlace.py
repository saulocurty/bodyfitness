from tkinter import *
from tkinter import ttk
from turtle import width
from tkinter import messagebox
from man_arquivos import *

class TelaMenu:
    def __init__(self, master=None):
        master.title("Menu")
        self.container1 = Frame(master, width=600, height=200)
        self.container1.place()

        self.container2 = Frame(master, bg='red')
        self.container2.place(x=250, y=250)

        self.container3 = Frame(master)
        self.container3.place()

        self.titulo =  Label(self.container1, text="MENU", font=("Arial", "20"))
        self.titulo.place(x=10, y=12)

        self.botao_add_a = Button(self.container2, text='Adicionar Alimento', width=15)
        self.botao_add_a.place(x=100, y=100)

        self.botao_add_e = Button(self.container2, text='Adicionar Exercicio', width=15)
        self.botao_add_e.place(x=10, y=55)

        self.botao_sel_a = Button(self.container2, text='Selecionar Alimento', width=15)
        self.botao_sel_a.place(x=10, y=40)

        self.botao_sel_e = Button(self.container2, text='Selecionar Exercicio', width=15)
        self.botao_sel_e.place(x=10, y=25)

        self.botao_rd = Button(self.container2, text='Resumo Diario', width=15, bg='red')
        self.botao_rd.place(x=10, y=10)









if __name__ == "__main__":     
    root = Tk()
    root.geometry("300x300") #tamanho da tela
    root.resizable(width=0, height=0)
    TelaMenu(root)
    root.mainloop()
