from tkinter import *
from tkinter import ttk
from telas.man_arquivos import *

class SelecionarAlimento:
    def __init__(self, master=None):
        master.title("Selecionar Alimento")

        with open('usuarios/Log.txt', 'r', encoding="utf8") as arquivo:
            usuario_logado = arquivo.read()
        self.usuario_logado = usuario_logado

        self.container1 = Frame(master)
        self.container1["pady"] = 20
        self.container1.grid(column=0, row=0, pady=(20, 20), padx=(50, 0))

        self.container2 = Frame(master)
        self.container2['pady'] = 0
        self.container2["padx"] = 10
        self.container2.grid(column=0, row=1)

        self.container3 = Frame(master)
        #self.container3['pady'] = 20
        self.container3.grid(column=0, row=2, pady=(20, 0))

        self.titulo = Label(self.container1, font=("Arial", "14", 'bold'), text='Selecionar Alimento') 
        self.titulo.grid(row=0, column=0, sticky='w', pady=(0,10))

        self.nome = Label(self.container2, font=("Arial", "12"), text='Alimento:')
        self.nome.grid(row=1, column=0, sticky='w', pady=(0, 20))
        self.comboVar = StringVar()
        self.comboAlimento = ttk.Combobox(self.container2, textvariable = self.comboVar, value=self.BuscaAlimentos(self.usuario_logado),width = 14, justify = 'center', font=('Arial', '10'), state = 'readonly') #mudar para usuario_logado
        self.comboAlimento.grid(column=1, row=1, sticky='w', pady=(0, 20))
        self.comboAlimento.current(0)

        self.caloria = Label(self.container2, font=("Arial", "12"), text='Quantidade(g):')
        self.caloria.grid(row=3, column=0, sticky='w')
        self.dado = Entry(self.container2, width=13, font=("Arial", "12"))
        self.dado.grid(row=3, column=1, sticky='w')

        self.botao_salvar = Button(self.container3, width=13, font=("Arial", "12"), text='Salvar',command = self.Acao)
        self.botao_salvar.grid(padx=(60, 0), pady=(30, 0))


    def BuscaAlimentos(self, email: str):
        path_l = f'usuarios/{email}/Tabela Alimentos.csv'
        Tabela = pd.read_csv(path_l, on_bad_lines='skip')
        Alimentos = Tabela['Alimentos']
        lista_alimentos = Alimentos.values.tolist()
        

        return lista_alimentos
    
    def Acao(self):
        alimento_selecionado = self.comboVar.get()
        grama = self.dado.get()
        if grama == '':
            grama = 0
        print(f"Grama = .{self.usuario_logado}.")
        Add_Alimento(alimento_selecionado, self.usuario_logado, grama)
    
if __name__ == '__main__':
    root = Tk()
    root.geometry("300x300") 
    root.resizable(width=0, height=0)
    SelecionarAlimento(root)
    root.mainloop()