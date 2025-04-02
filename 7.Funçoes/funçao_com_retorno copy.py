import os
os.system("clear")

def calcular_media( primeiro_numero , segundo_numero ):
    soma = primeiro_numero + segundo_numero
    media = soma / 2
    return media

primeiro_numero = int(input("Digite o primeiro numero: "))
segundo_numero = int(input("Digite o segundo numero: "))

media = calcular_media( primeiro_numero , segundo_numero )

print(f"Media: {media}")

