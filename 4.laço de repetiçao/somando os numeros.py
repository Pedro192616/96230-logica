import os

os.system("clear")

print("SOMANDO OS NUMEROS:")
soma = 0 
for i in range(5):
    nota = int(input("Digite um numero: "))
    soma = soma + nota 

print()
print(f"Soma: {soma}")

print("\nFIM DO PROGRAMA")