import os
os.system("clear")

def calcular_media( n1 , n2 ):
    soma = n1 + n2
    resultado = soma / 2
    return resultado

def aprovado_reprovado(media):
    if media >=7:
        print("Aprovado.")
    else:
        print("Reprovado.")
print("= NOTAS =")
n1 = int(input("Digite o primeiro numero: "))
n2 = int(input("Digite o segundo numero: "))

media = calcular_media(n1 , n2)
resultado = aprovado_reprovado(media)

print(f"Media: {media:.2f}")
print(resultado)

