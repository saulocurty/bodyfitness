from tkinter import *
from turtle import width
from man_arquivos import *
from tkinter import messagebox

class TelaRegistro:
    def __init__(self, master=None):
        master.title("Regsitro")

        self.container1 = Frame(master, bg='#00CED1')
        self.container1["padx"] = 50
        self.container1.grid(column=0, row=0, pady=(40, 0))

        self.container2 = Frame(master, bg='#00CED1')
        self.container2['pady'] = 20
        self.container2["padx"] = 10
        self.container2.grid(column=0, row=1)

        self.container3 = Frame(master, bg='#00CED1')
        #self.container3['pady'] = 20
        self.container3.grid(column=0, row=2)



        self.titulo = Label(self.container1, text="Registro", font=("Arial", "16","bold"), bg='#00CED1')
        self.titulo.grid(column=0, row=0, padx=(60, 0))

        self.nomeT = Label(self.container2, text="Nome", font=("Arial", "12"), bg='#00CED1')
        self.nomeT.grid(column=0, row=0, padx=(0,0))
        self.nome = Entry(self.container2, width=10, font=("Arial", "12"))
        self.nome.grid(column=1, row=0)

        self.idadeT = Label(self.container2, text="Idade", font=("Arial", "12"), bg='#00CED1')
        self.idadeT.grid(column=0, row=1)
        self.idade = Entry(self.container2, width=10, font=("Arial", "12"))
        self.idade.grid(column=1, row=1)

        self.emailT = Label(self.container2, text="Email", font=("Arial", "12"), bg='#00CED1')
        self.emailT.grid(column=0, row=2)
        self.email = Entry(self.container2, width=10, font=("Arial", "12"))
        self.email.grid(column=1, row=2)

        self.pesoT = Label(self.container2, text="Peso", font=("Arial", "12"), bg='#00CED1')
        self.pesoT.grid(column=0, row=3)
        self.peso = Entry(self.container2, width=10, font=("Arial"))
        self.peso.grid(column=1, row=3)

        self.generoT = Label(self.container2, text = 'Sexo', width=10, font=("Arial", '12'), bg='#00CED1')
        self.generoT.grid(column=0, row=4)
        self.genero = Entry(self.container2, width=10, font=("Arial"))
        self.genero.grid(column=1, row=4)


        self.botao1 = Button(self.container3, text="Registro", width=10, bg='#5F9EA0', relief=RAISED)
        self.botao1['command'] = self.Registrar
        self.botao1.grid(padx=(70, 0))

    def Registrar(self):
        user = Usuario(
            self.nome.get(),
            self.idade.get(),
            self.peso.get(),
            self.email.get(),
            self.genero.get()
        )
        g = self.genero.get()
        if(g.upper() != 'H' and g.upper() != 'M'):
            messagebox.showerror("Erro de Cadastro", "Digite F ou M no Campo 'Sexo'")
        else:
            if(Cria_Usuario(user)):
                messagebox.showinfo('Registrado', 'Parabens, voce esta Registrado')
                self.nome.delete(0,100)
                self.idade.delete(0, 100)
                self.peso.delete(0, 100)
                self.email.delete(0, 100)
                self.genero.delete(0, 100)




if __name__ == '__main__':    
    root = Tk()
    root.geometry("300x300") #tamanho da tela
    root.resizable(width=0, height=0)
    root.configure(bg='#00CED1')
    TelaRegistro(root)
    root.mainloop()