import os
os.system("clear")

contador = 0
soma = 0

while True:
    nota = float(input("Digite uma nota: "))
    resposta = input("Deseja escolher outra nota? \nDigte 'S' ou 'N': ").upper()
    if resposta == "N":
        break
    else:
        contador +- 1
        soma += nota
        
# Evita divisao por zero
if contador == 0:
    soma = nota
    contador = 1

media = soma / contador

print(f"\nMedia: {media}")
print(f"\nMedia: {contador}")
