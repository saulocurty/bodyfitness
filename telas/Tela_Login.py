from tkinter import *
from turtle import width
from tkinter import messagebox
from man_arquivos import *



class TelaLogin:
    def __init__(self, master=None):

        with open('log.txt', 'w') as log:
            pass


        self.container1 = Frame(master, bg='#00CED1')
        self.container1["pady"] = 20
        self.container1.grid(column=0, row=0, pady=(40, 0))

        self.container2 = Frame(master, bg='#00CED1')
        self.container2['pady'] = 20
        self.container2["padx"] = 100
        self.container2.grid(column=0, row=1)

        self.container3 = Frame(master, bg='#00CED1')
        #self.container3['pady'] = 20
        self.container3["padx"] = 110
        self.container3.grid(column=0, row=2)



        self.titulo = Label(self.container1, text="Login", font=("Sans", "19", 'bold'), bg='#00CED1')
        self.titulo.grid(column=0, row=0, pady=(0, 0), columnspan=2)

        self.nomeT = Label(self.container2, text="Email", font=("Times", "14", 'bold'), bg='#00CED1', fg='#800000')
        self.nomeT.grid(column=0, row=1)
        self.nome = Entry(self.container2, width=15, font=("Times", "12"),relief=SOLID)
        self.nome.grid(column=0, row=2, pady=(0, 0))

        self.botao1 = Button(self.container3, text="Login", width=10,relief=RAISED, bg='#5F9EA0')
        self.botao1["command"] = self.Logar
        self.botao1.grid()
        self.botao2 = Button(self.container3, text="Registro", width=10,relief=RAISED, bg='#5F9EA0')
        self.botao2.grid(pady=(10))

    def Logar(self):
        email_user = self.nome.get()
        if(not Verifica_Usuario(email_user)):
            messagebox.showerror("Erro Login", "Usuario Não Existe")
        else:
            with open('log.txt', 'w') as log:
                log.write(email_user)
            messagebox.showinfo('Logado', 'Parabens, voce esta logado')
            self.nome.delete(0, 100)

    





if __name__ == "__main__":     
    root = Tk()
    root.geometry("300x300") #tamanho da tela
    root.configure(bg='#00CED1')
    root.resizable(width=0, height=0)
    TelaLogin(root)
    root.mainloop()