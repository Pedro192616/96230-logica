import os
os.system("clear")

soma = 0
for i in range(3):
    while True:
        nota = float(input("Digite a nota do aluno: "))
        soma += nota
        break


def calcular_media(nota):
    media = soma / 3
    return media

media = calcular_media(nota)


print(f"Media: {media}")