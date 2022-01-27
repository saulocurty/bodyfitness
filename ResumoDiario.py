from tkinter import *
from turtle import width
from tkinter import messagebox
from tkinter import ttk
from atividades import *
from man_arquivos import *




class ResumoDiario:
    def __init__(self, master=None):
        master.title("Resumo")

        with open('usuarios/Log.txt', 'r', encoding="utf8") as arquivo:
            usuario_logado = arquivo.read()



        self.totalAlimentoCaloria = self.CalculaTotalA('sullo152@gmail.com')
        self.totalExercicioCaloria = 0
        

        self.div1 = Frame(master, bg='#00CED1')
        self.div1.grid(row=0, column=0, pady=(30, 30))
        self.div2 = Frame(master, bg='#00CED1')
        self.div2.grid(row=1, column=0)
        self.div3 = Frame(master, bg='#00CED1')
        self.div3.grid(row=2, column=0)




        self.totalA = Label(self.div2,text=f"Total {self.totalAlimentoCaloria}", font=('Arial', '14', 'bold'), bg='#00CED1')
        self.totalE = Label(self.div2,text=f"Total {self.totalExercicioCaloria}", font=('Arial', '14', 'bold'), bg='#00CED1')
        self.totalA.grid(row=2, column=0)
        self.totalE.grid(row=2, column=1)



        self.botaoV = Button(self.div3, width=15, text='Voltar',relief=RAISED, bg='#5F9EA0')
        self.botaoV.grid(column=0, row=2, padx=(30,0), pady=(30, 0))
        self.titulo = Label(self.div1, font=('Arial', '20', 'bold'), text='Resumo Diario', bg='#00CED1')
        self.titulo.grid(column=1, row=0)
        self.titulo2 =Label(self.div2, font=('Arial', '16', 'bold'), text='Calorias Consumidas', bg='#00CED1')
        self.titulo3 = Label(self.div2, font=('Arial', '16', 'bold'), text='Calorias Gastas', bg='#00CED1')
        self.titulo2.grid(row=0, column=0)
        self.titulo3.grid(row=0, column = 1)
        self.alimentosList = ttk.Treeview(self.div2,column=('nome', 'caloria'))
  
        self.alimentosList.heading("#0",text="")
        self.alimentosList.heading("nome",text="Nome")
        self.alimentosList.heading("caloria", text='Calorias')
        

        self.alimentosList.column("#0", width="0")
        self.alimentosList.column("nome", width="150")
        self.alimentosList.column("caloria", width="100")
        self.alimentosList.grid(row=1, column=0, padx=(40, 10))

        self.exerciciosList = ttk.Treeview(self.div2,column=('nome', 'caloria'))

        self.exerciciosList.heading("#0",text="")
        self.exerciciosList.heading("nome",text="Nome")
        self.exerciciosList.heading("caloria", text='Calorias')

        self.exerciciosList.column("#0", width="0")
        self.exerciciosList.column("nome", width="150")
        self.exerciciosList.column("caloria", width="100")
        self.exerciciosList.grid(row=1, column=1, padx=(0, 5))
        
        self.recomenda = Label(self.div3, text='Recomendações', font=('Sans', '16', 'bold'), bg='#00CED1')
        self.recomenda.grid(row=0, column=0, pady=(20, 10))
    

        self.Coluna_Alimento_Alimento('sullo152@gmail.com')


        self.recomenda_text = Message(self.div3, width=300, font=('sans', '14'), bg='#00CED1', justify=LEFT, fg='black', relief=SOLID)
        self.recomenda_text['text'] = 'Iai meus gostoso, como estão? vão se alimentar karalho'

        self.recomenda_text.grid(row=1, column=0)



    def Coluna_Alimento_Alimento(self, email: str):
        path_l =f'usuarios/sullo152@gmail.com/Alimentos Dia.csv'
        print("Buscando coluna alimentos...")
        Tabela = pd.read_csv(path_l)
        Alimentos = Tabela['Alimentos']
        Calorias = Tabela['Calorias']
        lista_alimentos = Alimentos.values.tolist()
        lista_calorias = Calorias.values.tolist()
        contador = 0
        total = 0
        for i, j in lista_alimentos,lista_calorias:
            self.alimentosList.insert(parent='', index=contador, values=(lista_alimentos[contador], lista_calorias[contador]))
            #total+= lista_calorias     
            contador+=1

        

    def CalculaTotalA(self, email: str):
        path_l =f'usuarios/{email}/Alimentos Dia.csv'
        
        Tabela = pd.read_csv(path_l)
        Calorias = Tabela['Calorias']
        lista_calorias = Calorias.values.tolist()
     
        total = 0
        for i in lista_calorias:
            print(i)
            total+= i    
          
        return total
        
        #print(lista_alimentos)
        #print(lista_exercicios)

    def CalculaTotalE(self, email: str):
        path_l =f'usuarios/{email}/Exercicio Dia.csv'
        
        Tabela = pd.read_csv(path_l)
        Calorias = Tabela['Calorias']
        lista_calorias = Calorias.values.tolist()
        
        total = 0
        for i in lista_calorias:
            
            total+= Calcula_Caloria_Total() 
            
        return total





if __name__ == "__main__":     
    root = Tk()
    root.geometry("600x600") #tamanho da tela
    root.configure(background='#00CED1')
    root.resizable(width=0, height=0)
    ResumoDiario(root)
    root.mainloop()