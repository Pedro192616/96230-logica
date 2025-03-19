import os
os.system("clear")

soma = 0

print("NOTAS:")
for i in range(4):
    nota = float(input("Digite uma nota: "))
    soma += nota

media = soma / 4

print()
print(f"Media: {media}")


print("\nFIM DO PROGRAMA")