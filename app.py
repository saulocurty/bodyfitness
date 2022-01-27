from man_arquivos import *
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

class Aplicacao:
    def __init__(self, master=None):
        master.title = "Aplicação"
    def CriaJanela():
        TelaLogin(Toplevel)

        



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





class SelecionarAlimento:
    def __init__(self, master=None):
        master.title("Selecionar Alimento")

        with open('usuarios/Log.txt', 'r', encoding="utf8") as arquivo:
            usuario_logado = arquivo.read()
        self.usuario_logado = usuario_logado
        self.user = Usuario('saulo', 19, 58, 'sullo152@gmail.com', 'm')

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
        print(f"Grama = .{usuario_logado}.")
        Add_Alimento(alimento_selecionado, self.usuario_logado, grama)
 
class SelecionarExercicio:
    def __init__(self, master=None):
        master.title("Selecionar Alimento")

        with open('usuarios/Log.txt', 'r', encoding="utf8") as arquivo:
            usuario_logado = arquivo.read()
        self.usuario_logado= usuario_logado
        self.user = Usuario('saulo', 19, 58, 'sullo152@gmail.com', 'm')

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

        self.titulo = Label(self.container1, font=("Arial", "14", 'bold'), text='Selecionar Exercicio')
        self.titulo.grid(row=0, column=0, sticky='w', pady=(0,10))

        self.nome = Label(self.container2, font=("Arial", "12"), text='Exercicio:')
        self.nome.grid(row=1, column=0, sticky='w', pady=(0, 20))
        self.exercicio = StringVar()
        self.comboExercicio = ttk.Combobox(self.container2, value=self.buscaExercicio(usuario_logado), textvariable = self.exercicio,width = 14, justify = 'center', font=('Arial', '10'), state = 'readonly') #mudar para usuario_logado
        self.comboExercicio.grid(column=1, row=1, sticky='w', pady=(0, 20))
        self.comboExercicio.current(0)

        self.caloria = Label(self.container2, font=("Arial", "12"), text='Tempo(Min):')
        self.caloria.grid(row=3, column=0, sticky='w')
        self.dado = Entry(self.container2, width=13, font=("Arial", "12"))
        self.dado.grid(row=3, column=1, sticky='w')

        self.botao_salvar = Button(self.container3, width=13, font=("Arial", "12"), text='Salvar', command=self.Acao)
        self.botao_salvar.grid(padx=(60, 0), pady=(30, 0))


    def buscaExercicio(self, email: str):
        path_l = f'usuarios/{email}/Tabela Exercicio.csv'
        Tabela = pd.read_csv(path_l,  on_bad_lines='skip')
        Exercicio = Tabela['Exercicio']
        listaExercicios = Exercicio.values.tolist()

        return listaExercicios

    def Acao(self):
        exercicio_selecionado = self.exercicio.get()
        tempo = self.dado.get()
        Add_Exercicio(exercicio_selecionado, self.usuario_logado, int(tempo))
    

        
class TelaLogin:
    def __init__(self, master=None):
        master.title("Login")

        with open('usuarios/log.txt', 'w') as log:
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
            with open('usuarios/log.txt', 'w') as log:
                log.write(email_user)
            messagebox.showinfo('Logado', 'Parabens, voce esta logado')
            self.nome.delete(0, 100)


class TelaMenu:
    def __init__(self, master=None):
        master.title("Menu")

        with open('usuarios/Log.txt', 'r', encoding="utf8") as arquivo:
            usuario_logado = arquivo.read()

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




class TelaRegistro:
    def __init__(self, master=None):
        master.title("Regsitro")

        self.container1 = Frame(master)
        self.container1["padx"] = 50
        self.container1.grid(column=0, row=0, pady=(40, 0))

        self.container2 = Frame(master)
        self.container2['pady'] = 20
        self.container2["padx"] = 10
        self.container2.grid(column=0, row=1)

        self.container3 = Frame(master)
        #self.container3['pady'] = 20
        self.container3.grid(column=0, row=2)



        self.titulo = Label(self.container1, text="Registro", font=("Arial", "16"))
        self.titulo.grid(column=0, row=0, padx=(60, 0))

        self.nomeT = Label(self.container2, text="Nome", font=("Arial", "12"))
        self.nomeT.grid(column=0, row=0, padx=(0,0))
        self.nome = Entry(self.container2, width=10, font=("Arial", "12"))
        self.nome.grid(column=1, row=0)

        self.idadeT = Label(self.container2, text="Idade", font=("Arial", "12"))
        self.idadeT.grid(column=0, row=1)
        self.idade = Entry(self.container2, width=10, font=("Arial", "12"))
        self.idade.grid(column=1, row=1)

        self.emailT = Label(self.container2, text="Email", font=("Arial", "12"))
        self.emailT.grid(column=0, row=2)
        self.email = Entry(self.container2, width=10, font=("Arial", "12"))
        self.email.grid(column=1, row=2)

        self.pesoT = Label(self.container2, text="Peso", font=("Arial", "12"))
        self.pesoT.grid(column=0, row=3)
        self.peso = Entry(self.container2, width=10, font=("Arial"))
        self.peso.grid(column=1, row=3)

        self.generoT = Label(self.container2, text = 'Sexo', width=10, font=("Arial", '12'))
        self.generoT.grid(column=0, row=4)
        self.genero = Entry(self.container2, width=10, font=("Arial"))
        self.genero.grid(column=1, row=4)


        self.botao1 = Button(self.container3, text="Registro", width=10)
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




root = Tk()
Aplicacao(root)
root.mainloop()