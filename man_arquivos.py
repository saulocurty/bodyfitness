from distutils.log import error
import pandas as pd
import csv
import asyncio
import os
import shutil



class Alimento:
    def __init__(self, nome : str,  calorias:str):
        self.nome = nome
        self.calorias = calorias



class Usuario:
    def __init__(self, nome:str, idade:int, peso:int, email:str, genero:str):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.email = email
        self.genero = genero
    
    def Muda_Dados(self, nome: str = '-1', idade : int=-1, peso: int=-1, email: str='-1', genero: str='-1'):
        self.nome = self.nome if nome == '-1' else nome
        self.idade = self.idade if idade == -1 else idade
        self.peso = self.peso if peso == -1 else peso
        self.email = self.email if email == '-1' else email
        self.genero - self.genero if genero == '-1' else genero

    
def Verifica_Usuario(Usuario):
    nome_busca = Usuario.nome
    email_busca = Usuario.email
    return Busca_Usuario_Tabela(Usuario.nome, Usuario.email)

def Busca_Usuario_Tabela(usuario:str, email:str):
    Tabela = pd.read_csv('usuarios/Usuarios.csv')

    Emails = Tabela["Email"]

    for i in Emails:
        if (i.lower() == email.lower()):
            print("Email encontrado")
            return 1
    return 0

def Cria_Usuario(Usuario):
    if(Verifica_Usuario(Usuario)):
        print("Usuario ja existe")
        return 0
    else:    
        with open('usuarios/Usuarios.csv',"a", newline='', encoding="utf-8") as csv_file:
            arquivo = csv.writer(csv_file, delimiter=',', quoting=csv.QUOTE_MINIMAL)
            arquivo.writerow([Usuario.email, Usuario.nome, Usuario.idade, Usuario.peso, Usuario.genero])
            print("Usuario Criado")
            #verifica se ja existe o usuario
        
        tabela1 = os.path.abspath('.') + '/originais/Exercicio Dia.csv'
        tabela2 = os.path.abspath('.') + '/originais/Alimentos Dia.csv'
        diretorio = Usuario.email
        diretorio2 = os.path.abspath('.') + '/originais/Tabela Alimentos.csv'
        diretorio3 = os.path.abspath('.') + '/originais/Tabela Exercicio.csv'
        meu_path = os.path.abspath('.') + '/usuarios/' + diretorio 
        os.mkdir(meu_path)
        shutil.copy(diretorio2, meu_path)
        shutil.copy(diretorio3, meu_path)
        shutil.copy(tabela1, meu_path)
        shutil.copy(tabela2, meu_path)
        return 1
 
def Deleta_Usuario(Usuario):
    pass


def Verifica_Alimento(user : Usuario, nome: str): #modificar depois
    path_l = path_l = f'usuarios/{user.email}/Tabela Alimentos.csv'
    Table = pd.read_csv(path_l)
    Alimentos = Table['Alimentos']
    for i in Alimentos:
        print('--- i = ', i, 'alimento compara = ', nome) #debug
        if(i.lower() == nome.lower()):
            print("Alimento encontrado")
            return 1
    return 0


def Inserir_Aliemento(user: Usuario, comida: Alimento):
    path_l = f'usuarios/{user.email}/Tabela Alimentos.csv'
    if(Verifica_Alimento(user, comida.nome)):
        print("Alimento ja existe")
        return
    else:
         with open(path_l,"a", newline='', encoding="utf-8") as csv_file:
            arquivo = csv.writer(csv_file, delimiter=',', quoting=csv.QUOTE_MINIMAL)
            arquivo.writerow([comida.nome, comida.calorias])
            print("Alimento Criado")
            #verifica se ja existe o usuario


def Remover_Alimento(user: Usuario, comida: Alimento):
    pass


def Login(user: Usuario):
    if(Verifica_Usuario(user)):
        print("Voce esta logado!")
        return 1
    else:
        print("Usuario não registrado")
        return 0

def Seleciona_Alimento( nome: str, email: str): #modificar depois
    alimento_string = ''
    path_l = f'usuarios/{email}/Tabela Alimentos.csv'
    Table = pd.read_csv(path_l)
    Alimentos = Table['Alimentos']
    
    contador = 0
    for i in Alimentos:
        if(i.lower() == nome.lower()):
            x = Table.loc[[contador]].to_string(header=False, index=False, index_names=False)
            nova = x.split(' ')
            alimento_string = ','.join(nova)
            print(alimento_string)#debug
            return alimento_string
        contador = contador + 1
    return 0


def Adiciona_Alimento_Dia(ex: str, email: str):
    nome = Seleciona_Alimento(ex, email)
    nomeA = ''
    nomeB = ''
    controle = 0
    for element in nome: 
        if element == ',':
            controle = 1
            continue
        elif controle == 1:
            nomeB = nomeB + element
        elif controle == 0: 
            nomeA = nomeA + element

    pathL =  f'usuarios/{email}/Alimentos Dia.csv'

    with open(pathL,"a", newline='', encoding="utf-8") as csv_file:
            arquivo = csv.writer(csv_file, delimiter=',', quoting=csv.QUOTE_MINIMAL)
            arquivo.writerow([nomeA, nomeB])
            print("Alimento Criado") 


def Seleciona_Exercicio(nome: str, email : str):
    exercicio_string = ''
    path_l = f'usuarios/{email}/Tabela Exercicio.csv'
    Table = pd.read_csv(path_l)
    Exercicios = Table['Atividade 30 minutos']
    #print(Exercicios)
    
    contador = 0
    for i in Exercicios:
        if(i.lower() == nome.lower()):
            x = Table.loc[[contador]].to_string(header=False, index=False, index_names=False)
            nova = x.split(' ')
            #alimento_string = ','.join(nova)
            #print(alimento_string)#debug
            return nova
        contador = contador + 1
    return 0

def Adiciona_Exercicio_Dia(ex: str, email: str):
    nome = Seleciona_Exercicio(ex, email)
    pathL = f'usuarios/{email}/Exercicio Dia.csv'
    with open(pathL,"a", newline='', encoding="utf-8") as csv_file:
            arquivo = csv.writer(csv_file, delimiter=',', quoting=csv.QUOTE_MINIMAL)
            arquivo.writerow([nome[0], nome[1], nome[2]])
            print("Exercicio Criado") 


if __name__ == '__main__':    
    Adiciona_Exercicio_Dia('Dança', 'sullo152@gmail.com')