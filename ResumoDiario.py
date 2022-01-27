from tkinter import *
from turtle import width
from tkinter import messagebox
from tkinter import ttk
from man_arquivos import *



class ResumoDiario:
    def __init__(self, master=None):
        master.title("Resumo")
        
        self.div1 = Frame(master, bg='#00CED1')
        self.div1.grid(row=0, column=0, pady=(30, 30))
        self.div2 = Frame(master, bg='#00CED1')
        self.div2.grid(row=1, column=0)
        self.div3 = Frame(master, bg='#00CED1')
        self.div3.grid(row=2, column=0)


        self.botaoV = Button(self.div3, width=15, text='Voltar',relief=RAISED, bg='#5F9EA0')
        self.botaoV.grid(column=0, row=2, padx=(30,0), pady=(30, 0))
        self.titulo = Label(self.div1, font=('Arial', '20', 'bold'), text='Resumo Diario', bg='#00CED1')
        self.titulo.grid(column=1, row=0)
        self.titulo2 =Label(self.div2, font=('Arial', '16', 'bold'), text='Calorias Consumidas', bg='#00CED1')
        self.titulo3 = Label(self.div2, font=('Arial', '16', 'bold'), text='Calorias Gastas', bg='#00CED1')
        self.titulo2.grid(row=0, column=0)
        self.titulo3.grid(row=0, column = 1)
        self.alimentosList = ttk.Treeview(self.div2,column=('nome', 'caloria', 'total'))
  
        self.alimentosList.heading("#0",text="")
        self.alimentosList.heading("nome",text="Nome")
        self.alimentosList.heading("caloria", text='Calorias')
        self.alimentosList.heading("total", text='Total')

        self.alimentosList.column("#0", width="0")
        self.alimentosList.column("nome", width="130")
        self.alimentosList.column("caloria", width="70")
        self.alimentosList.column("total", width="70")
        self.alimentosList.grid(row=1, column=0, padx=(22, 10))

        self.exerciciosList = ttk.Treeview(self.div2,column=('nome', 'caloria', 'total'))

        self.exerciciosList.heading("#0",text="")
        self.exerciciosList.heading("nome",text="Nome")
        self.exerciciosList.heading("caloria", text='Calorias')
        self.exerciciosList.heading("total", text='Total')

        self.exerciciosList.column("#0", width="0")
        self.exerciciosList.column("nome", width="130")
        self.exerciciosList.column("caloria", width="70")
        self.exerciciosList.column("total", width="70")
        self.exerciciosList.grid(row=1, column=1, padx=(0, 5))
        
        self.recomenda = Label(self.div3, text='Recomendações', font=('Sans', '16', 'bold'), bg='#00CED1')
        self.recomenda.grid(row=0, column=0, pady=(20, 10))
        
        self.recomenda_text = Message(self.div3, width=300, font=('sans', '14'), bg='#00CED1', justify=LEFT, fg='black')
        self.recomenda_text['text'] = 'Iai meus gostoso, como estão? vão se alimentar karalho'

        self.recomenda_text.grid(row=1, column=0)

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