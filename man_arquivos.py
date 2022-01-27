from calendar import c
from distutils.log import error
import pandas as pd
import csv
import asyncio
import os
import shutil
from atividades import *
from tkinter import *

root = Tk()

class Exercicio:
    def __init__(self, nome:str, caloria: int):
        self.nome = nome
        self.caloria = caloria
        




class Alimento:
    def __init__(self, nome : str,  calorias: str):
        self.nome = nome
        self.caloria =  calorias
        



class Usuario:
    def __init__(self, nome:str, idade:int, peso:int, email:str, genero:str):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.email = email
        self.genero = genero.lower()
    
    def Muda_Dados(self, nome: str = '-1', idade : int=-1, peso: int=-1, email: str='-1', genero: str='-1'):
        self.nome = self.nome if nome == '-1' else nome
        self.idade = self.idade if idade == -1 else idade
        self.peso = self.peso if peso == -1 else peso
        self.email = self.email if email == '-1' else email
        self.genero - self.genero if genero == '-1' else genero


usuario_logado = ''
user_logado = Usuario('', 0, 0,'','')

def Verifica_Usuario(email: str):
    email_busca = email
    return Busca_Usuario_Tabela(email)

def Busca_Usuario_Tabela(email:str):
    Tabela = pd.read_csv('usuarios/Usuarios.csv')

    Emails = Tabela["Email"]

    for i in Emails:
        if (i.lower() == email.lower()):
            print("Email encontrado")
            return 1
    return 0

def Cria_Usuario(user: Usuario):
    if(Verifica_Usuario(user.email)):
        print("Usuario ja existe")
        return 0
    else:    
        with open('usuarios/Usuarios.csv',"a+", newline='', encoding="utf-8") as csv_file:
            arquivo = csv.writer(csv_file, delimiter=',', quoting=csv.QUOTE_MINIMAL,lineterminator='\n')
            arquivo.writerow([user.email, user.nome, user.idade, user.peso, user.genero])
            print("Usuario Criado")
            #verifica se ja existe o usuario
        
        tabela1 = os.path.abspath('.') + '/originais/Exercicio Dia.csv'
        tabela2 = os.path.abspath('.') + '/originais/Alimentos Dia.csv'
        diretorio = user.email
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


def Verifica_Exercicio(nome: str, email: str):
    path_l = path_l = f'usuarios/{email}/Tabela Exercicio.csv'
    print("To na verifica E")
    print(path_l)
    Tabela = pd.read_csv(path_l)
    Exercicios = Tabela['Atividade 30 minutos']
    for i in Exercicios:
        print('--- i = ', i, 'alimento compara = ', nome) #debug
        if(i.lower() == nome.lower()):
            print("Exercicio encontrado")
            return 1
    return 0

def Inserir_Exercicio(email: str, exercicio: Exercicio):
    path_l = f'usuarios/{email}/Tabela Exercicio.csv'
    if(Verifica_Exercicio(exercicio.nome, email)):
        print("Exercicio Ja existe")
        return
    else:
         with open(path_l,"a+", newline='', encoding="utf-8") as csv_file:
            arquivo = csv.writer(csv_file, delimiter=',', quoting=csv.QUOTE_MINIMAL,lineterminator='\n')
            arquivo.writerow([exercicio.nome, exercicio.caloriaH, exercicio.caloriaM])
            print("Exercicio Criado")
            #verifica se ja existe o usuario

def Verifica_Alimento(email: str, nome: str): #modificar depois
    path_l = path_l = f'usuarios/{email}/Tabela Alimentos.csv'
    print("To na verifica")
    print(path_l)
    Tabela = pd.read_csv(path_l)
    Alimentos = Tabela['Alimentos']
    for i in Alimentos:
        print('--- i = ', i, 'alimento compara = ', nome) #debug
        if(i.lower() == nome.lower()):
            print("Alimento encontrado")
            return 1
    return 0


def Inserir_Alimento(email: str, comida: Alimento):
    path_l = f'usuarios/{email}/Tabela Alimentos.csv'
    if(Verifica_Alimento(email, comida.nome)):
        print("Alimento ja existe")
        return
    else:
         with open(path_l,"a+", newline='', encoding="utf-8") as csv_file:
            arquivo = csv.writer(csv_file, delimiter=',', quoting=csv.QUOTE_MINIMAL,lineterminator='\n')
            arquivo.writerow([comida.nome, comida.calorias])
            print("Estou na INserir Alimentos e adicionei o aliemnto")
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

    with open(pathL,"a+", newline='', encoding="utf-8") as csv_file:
            arquivo = csv.writer(csv_file, delimiter=',', quoting=csv.QUOTE_MINIMAL,lineterminator='\n')
            arquivo.writerow([nomeA, nomeB])
            print("Alimento Criado") 


def Seleciona_Exercicio(nome: str, email : str):
    exercicio_string = ''
    path_l = f'usuarios/{email}/Tabela Exercicio.csv'
    Table = pd.read_csv(path_l)
    Exercicios = Table['Atividade 30 minutos']
    
    
    contador = 0
    for i in Exercicios:
        if(i.lower() == nome.lower()):
            x = Table.loc[[contador]].to_string(header=False, index=False, index_names=False)
            nova = x.split(' ')
            return nova
        contador = contador + 1
    return 0

def Adiciona_Exercicio_Dia(ex: str, email: str):
    nome = Seleciona_Exercicio(ex, email)
    pathL = f'usuarios/{email}/Exercicio Dia.csv'
    with open(pathL,"a+", newline='', encoding="utf-8") as csv_file:
            arquivo = csv.writer(csv_file, delimiter=',', quoting=csv.QUOTE_MINIMAL,lineterminator='\n')
            arquivo.writerow([nome[0], nome[1], nome[2]])
            print("Exercicio Criado") 

def Add_Alimento(nome: str, email:str, grama: int):
    pathR = f'usuarios//{email}//Tabela Alimentos.csv'
    pathL = f'usuarios//{email}//Alimentos Dia.csv'
    Tabela = pd.read_csv(pathR,engine= 'python', on_bad_lines='skip')
    Tabela2 = Tabela['Alimentos']
    print(Tabela2)
    contador = 0
    for i in Tabela2:
        if i.lower() == nome.lower():
            break
        contador+=1

    caloria = Tabela.loc[contador]['Calorias'].item()

    calorias = (int(grama) * caloria)/100

    with open(pathL,"a+", newline='', encoding="utf-8") as csv_file:
            arquivo = csv.writer(csv_file, delimiter=',', quoting=csv.QUOTE_MINIMAL,lineterminator='\n')
            arquivo.writerow([nome, calorias])
            print("Alimento Criado") 


def Add_Exercicio(nome: str, email:str, tempo: int):
    pathR = f'usuarios//{email}//Tabela Exercicio.csv'
    pathL = f'usuarios//{email}//Exercicio Dia.csv'
    Tabela = pd.read_csv(pathR,engine= 'python', on_bad_lines='skip')
    Tabela2 = Tabela['Exercicio'].tolist()
    contador = 0
    for i in Tabela2:
        print(f"i = {i}")
        print(f"nome = {nome}")
        if i.lower() == nome:
            break
        contador+=1

    caloria = Tabela.loc[contador]['Calorias'].item()
    print(f" o timpo de caloria é {type(caloria)}, tempo = {type(tempo)} ")
    calorias = (caloria * tempo)/ 30

    with open(pathL,"a+", newline='', encoding="utf-8") as csv_file:
            arquivo = csv.writer(csv_file, delimiter=',', quoting=csv.QUOTE_MINIMAL,lineterminator='\n')
            arquivo.writerow([nome, calorias])
            print("Exercicio Criado") 




if __name__ == '__main__':    
    #Adiciona_Exercicio_Dia('Dança', 'sullo152@gmail.com')
    pass