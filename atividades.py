from man_arquivos import *

def CalculaBEE(idade: int, genero: str,peso: int, altura=1.7):
    calorias = 0
    if idade >= 0 and idade < 19:

        if genero == 'm':
            calorias = 68 - 43.3 * idade + 712 * altura + 19.2 * peso
        else:
            calorias = 189 - 17.6 * idade + 625 * altura + 7.9 * peso

    elif (idade >= 19):
        if genero == 'm':
                calorias = 204 - 4 * idade + 450.5 * altura + 11.69 * peso
        else:
            calorias = 255 - 2.35 * idade + 361.6 * altura + 9.39 * peso
    
    return calorias

