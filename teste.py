

a = ''

with open('usuarios/Log.txt', 'r', encoding="utf8") as arquivo:
    a = arquivo.read()
    print(type(a))