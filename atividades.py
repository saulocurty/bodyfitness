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


def Calcula_Caloria_Exercicio(exercicio: str, user_genero: str, idade:int, email:str ):
    caloria = 0
    if exercicio == 'caminhada':
        caloria = 55
        if user_genero.lower() == 'h':
            caloria += 14
        else:
            caloria-=14
        fator = (int((70 - idade)/10)) * 4
        return fator+caloria


    elif exercicio == 'ciclismo':
        caloria = 73
        if user_genero.lower() == 'h':
            caloria += 10
        else:
            caloria-=10
        fator = (int((70 - idade)/10)) * 3
        return fator+caloria
        
    elif exercicio == 'corrida':
        caloria = 293
        if user_genero.lower() == 'h':
            caloria += 38
        else:
            caloria-=38
        fator = (int((70 - idade)/10)) * 8
        return fator+caloria


    elif exercicio == 'natação':
        caloria = 110
        if user_genero.lower() == 'h':
            caloria += 21
        else:
            caloria-=21
        fator = (int((70 - idade)/10)) * 6
        return fator+caloria
  

    elif exercicio == 'musculação':
        caloria = 110
        if user_genero.lower() == 'h':
            caloria += 21
        else:
            caloria-=21
        fator = (int((70 - idade)/10)) * 6
        return fator+caloria


    elif exercicio == 'dança':
        caloria = 133
        if user_genero.lower() == 'h':
            caloria += 25
        else:
            caloria-=25
        fator = (int((70 - idade)/10)) * 7
        return fator+caloria

    elif exercicio == 'futebol':
        caloria = 128
        if user_genero.lower() == 'h':
            caloria += 24       
        else:
            caloria-=24
        fator = (int((70 - idade)/10)) * 8
        return fator+caloria
 

    elif exercicio == 'basquete':
        caloria = 110
        if user_genero.lower() == 'h':
            caloria += 21
        else:
            caloria-=21
        fator = (int((70 -idade)/10)) * 6
        return fator+caloria


    elif exercicio == 'pular corda':
        caloria = 161
        if user_genero.lower() == 'h':
            caloria += 30
        else:
            caloria-=30
        fator = (int((70 - idade)/10)) * 9
        return fator + caloria


    elif exercicio == 'limpar a casa':
        caloria = 60
        if user_genero.lower() == 'h':
            caloria += 9
        else:
            caloria-=9
        fator = (int((70 - idade)/10)) * 3 
        return fator + caloria

    else:
        pass

def Calcula_Caloria_Total(user: str, exer: str, idade: int, genero: str, peso: int, email:str):
    total = Calcula_Caloria_Exercicio(exer, genero, idade, email)
    total+= CalculaBEE(idade, genero, peso)
    return total
