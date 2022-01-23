from distutils.log import error
import pandas as pd
import csv
import asyncio
import os

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
    return 

def Cria_Usuario(Usuario):
    if(Verifica_Usuario(Usuario)):
        print("Usuario ja existe")
        return
    else:    
        with open('usuarios/Usuarios.csv',"a", newline='') as csv_file:
            arquivo = csv.writer(csv_file, delimiter=',', quoting=csv.QUOTE_MINIMAL)
            arquivo.writerow([Usuario.email, Usuario.nome, Usuario.idade, Usuario.peso, Usuario.genero])
            print("Usuario Criado")
            #verifica se ja existe o usuario
        
        diretorio = Usuario.email
        meu_path = os.path.abspath('.') + '/usuarios/' + diretorio 
        os.mkdir(meu_path)
 
def Deleta_Usuario(Usuario):
    with open('')


Saulo = Usuario("AGles", 16, 48, "saulo@gmail.com", "M")
#Cria_Usuario(Saulo)
Deleta_Usuario(Saulo)
#print(Busca_Usuario_Tabela(Saulo.nome, Saulo.email))





