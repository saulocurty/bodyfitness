from tkinter import *
from turtle import width
from tkinter import messagebox
from tkinter import ttk
from man_arquivos import *



class ResumoDiario:
    def __init__(self, master=None):
        master.title("Resumo")
        
        self.div1 = Frame(master, bg='#00CED1')
        self.div1.grid(row=0, column=0)
        self.div2 = Frame(master, bg='#00CED1')
        self.div2.grid(row=1, column=0)
        self.div3 = Frame(master)
        self.div3.grid(row=2, column=0)



        self.titulo = Label(self.div1, font=('Arial', '16', 'bold'), text='Resumo Diario', bg='#00CED1')
        self.titulo.grid(column=0, row=0)

        self.alimentosList = ttk.Treeview(self.div2,column=('#0','nome', 'caloria', 'total'))
  
        self.alimentosList.heading("#0",text="")
        self.alimentosList.heading("nome",text="Nome")
        self.alimentosList.heading("caloria", text='Calorias')
        self.alimentosList.heading("total", text='Total')

        self.alimentosList.column("#0", width="0")
        self.alimentosList.column("nome", width="200")
        self.alimentosList.column("caloria", width="50")
        self.alimentosList.column("total", width="50")
        self.alimentosList.grid()
        
        #self.exercicioList = ttk.Treeview(self.div2, height=3, column=())
        
        

    def Coluna_Alimento_Alimento(self, email: str):
        path_l = path_l = f'usuarios/{email}/Exercicio Dia.csv'
        print("Buscando coluna alimentos...")
        Tabela = pd.read_csv(path_l)
        Alimentos = Tabela['Alimentos']
        lista_alimentos = Alimentos.values.tolist()

        return tuple(lista_alimentos)






if __name__ == "__main__":     
    root = Tk()
    root.geometry("600x600") #tamanho da tela
    root.configure(background='#00CED1')
    root.resizable(width=0, height=0)
    ResumoDiario(root)
    root.mainloop()