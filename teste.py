import pandas as pd
import csv

path_l = path_l = f'usuarios/sullo152@gmail.com/Tabela Alimentos.csv'
print("To na verifica")
print(path_l)
Tabela = pd.read_csv(path_l)
Alimentos = Tabela['Alimentos']
lista_alimentos = Alimentos.values.tolist()

print(Alimentos)
print(lista_alimentos)