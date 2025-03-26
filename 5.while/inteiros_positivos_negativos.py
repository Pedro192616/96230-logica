import os 
os.system("clear")

contador = 1
soma = 0

while True:
    nota = int(input(f"Digite o {contador + 1}º numero: "))
    if nota < 0:
        break
    else:
        contador +- 1 
        soma += nota


media = soma / contador

print(f"\nMedia: {media}")
print(f"\nMedia: {contador}")

