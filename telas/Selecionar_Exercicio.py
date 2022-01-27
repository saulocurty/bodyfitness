from tkinter import *
from tkinter import ttk
from man_arquivos import *
import pandas as pd



class SelecionarExercicio:
    def __init__(self, master=None):
        master.title("Selecionar Alimento")

        usuario_logado = 'asda'
        self.usuario_logado= usuario_logado
        self.user = Usuario('saulo', 19, 58, 'sullo152@gmail.com', 'm')

        self.container1 = Frame(master,bg='#00CED1')
        self.container1["pady"] = 20
        self.container1.grid(column=0, row=0, pady=(20, 20), padx=(50, 0))

        self.container2 = Frame(master,bg='#00CED1')
        self.container2['pady'] = 0
        self.container2["padx"] = 10
        self.container2.grid(column=0, row=1)

        self.container3 = Frame(master,bg='#00CED1')
        #self.container3['pady'] = 20
        self.container3.grid(column=0, row=2, pady=(20, 0))

        self.titulo = Label(self.container1, font=("Arial", "14", 'bold'), text='Selecionar Exercicio',bg='#00CED1')
        self.titulo.grid(row=0, column=0, sticky='w', pady=(0,10))

        self.nome = Label(self.container2, font=("Arial", "12"), text='Exercicio:',bg='#00CED1')
        self.nome.grid(row=1, column=0, sticky='w', pady=(0, 20))
        self.exercicio = StringVar()
        self.exercicio.set("caminhada")
        self.comboExercicio = ttk.Combobox(self.container2, value=self.buscaExercicio(usuario_logado), textvariable = self.exercicio,width = 14, justify = 'center', font=('Arial', '10'), state = 'readonly') #mudar para usuario_logado
        self.comboExercicio.grid(column=1, row=1, sticky='w', pady=(0, 20))


        self.caloria = Label(self.container2, font=("Arial", "12"), text='Tempo(Min):',bg='#00CED1')
        self.caloria.grid(row=3, column=0, sticky='w')
        self.dado = Entry(self.container2, width=13, font=("Arial", "12"))
        self.dado.grid(row=3, column=1, sticky='w')

        self.botao_salvar = Button(self.container3, width=13, font=("Arial", "12"), text='Salvar', command=self.Acao ,relief=RAISED, bg='#5F9EA0')
        self.botao_salvar.grid(padx=(60, 0), pady=(30, 0))


    def buscaExercicio(self, email: str):
        path_l = f'usuarios/{email}/Tabela Exercicio.csv'
        Tabela = pd.read_csv(path_l,  on_bad_lines='skip')
        Exercicio = Tabela['Exercicio']
        listaExercicios = Exercicio.values.tolist()

        return listaExercicios

    def Acao(self):
        exercicio_selecionado = self.exercicio.get()
        print(f'exer selc {exercicio_selecionado}')
        tempo = self.dado.get()
        Add_Exercicio(exercicio_selecionado, self.usuario_logado, int(tempo))
    

        
    
if __name__ == '__main__':
    root = Tk()
    root.geometry("300x300") #tamanho da tela
    root.resizable(width=0, height=0)
    root.configure(bg='#00CED1')
    SelecionarExercicio(root)
    root.mainloop()