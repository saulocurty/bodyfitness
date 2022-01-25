import pandas as pd
import csv


nome = 'alho,67'
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

print('A = ', nomeA, 'B = ', nomeB)