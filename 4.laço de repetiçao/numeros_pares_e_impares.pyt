import os
os.system("clear")

pares = 0 
impares = 0

print("NUMEROS PARES E IMPARES")
for i in range (5):
    numero = int(input("Digite um numero:  "))
    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1


print()
print(f"Pares: {pares}")
print(f"impares: {impares}")

print("\nFIM DO PROGRAMA")