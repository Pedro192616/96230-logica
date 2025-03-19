import os
os.system("clear")

soma = 0

print("NOTAS:")
for i in range(3):
    nota = float(input("Digite uma nota: "))
    soma += nota
    media = soma / 3

if media >= 7:
    print("Aprovado.")

elif media - 4 :
    print("Reprovado.")

print()
print(f"Media: {media}")
