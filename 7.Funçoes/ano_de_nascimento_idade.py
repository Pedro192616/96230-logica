import os
os.system("clear")

def calcular(ano_nascimento):

    if ano_nascimento:
        resultado = ano_atual - ano_nascimento
    return resultado


ano_nascimento = int(input("Digite o ano de nascimento: "))
ano_atual = int(input("Digite o ano atual: "))
resultado = calcular (ano_nascimento)
print(f"Sua idade e de {resultado} anos.")