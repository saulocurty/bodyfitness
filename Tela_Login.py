from tkinter import *
from turtle import width
from tkinter import messagebox
from man_arquivos import *



class TelaLogin:
    def __init__(self, master=None):
        master.title("LOGIN")

        self.container1 = Frame(master)
        self.container1["pady"] = 20
        self.container1.grid(column=0, row=0, pady=(40, 0))

        self.container2 = Frame(master)
        self.container2['pady'] = 20
        self.container2["padx"] = 110
        self.container2.grid(column=0, row=1)

        self.container3 = Frame(master)
        #self.container3['pady'] = 20
        self.container3["padx"] = 110
        self.container3.grid(column=0, row=2)



        self.titulo = Label(self.container1, text="Login", font=("Arial", "16"))
        self.titulo.grid(column=0, row=0, pady=(0, 0))

        self.nomeT = Label(self.container2, text="Email", font=("Arial", "12"))
        self.nomeT.grid(column=0, row=1)
        self.nome = Entry(self.container2, width=10, font=("Arial", "12"))
        self.nome.grid(column=0, row=2)

        self.botao1 = Button(self.container3, text="Login", width=10)
        self.botao1["command"] = self.Logar
        self.botao1.grid()
        self.botao2 = Button(self.container3, text="Registro", width=10)
        self.botao2.grid()

    def Logar(self):
        email_user = self.nome.get()
        A = Usuario('a', 19, 99, email_user, 'm')
        if(not Verifica_Usuario(A)):
            messagebox.showerror("Erro Login", "Usuario Não Existe")
        else:
            messagebox.showinfo('Logado', 'Parabens, voce esta logado')

    





if __name__ == "__main__":     
    root = Tk()
    root.geometry("300x300") #tamanho da tela
    root.resizable(width=0, height=0)
    TelaLogin(root)
    root.mainloop()