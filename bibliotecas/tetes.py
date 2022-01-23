import os
import csv

print(os.path.abspath('.'))


def Deleta_Usuario(Usuario):
    linhas = list()
    with open('usuarios/Usuarios.csv', 'r') as csv_file:
        reader = csv.reader(csv_file, delimiter=',')
        for row in reader:
            linhas.append(row)
            for field in row:
                if field == Usuario.email:
                    linhas.remove(row)
    with open('usuarios/Usuarios.csv', 'w') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(linhas)
