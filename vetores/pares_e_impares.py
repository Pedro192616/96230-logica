import os
os.system("clear")


lista_numeros = []
QUANTIDADE_NUMEROS = 6



def pares_impares(lista_numeros):
    pares = 0
    impares = 0

    for numero in (lista_numeros):
        if numero % 2 == 0:
            pares +=1
    else:
            impares +=1
    return pares , impares

for i in range(QUANTIDADE_NUMEROS):
    numero = float(input(f"Digite o {i+1}º numero: "))
    lista_numeros.append(numero)



pares , impares = pares_impares(lista_numeros)

print("\nMostrando numeros")
for i,numero in enumerate(lista_numeros, start=1):
     print(f"{i}º numero: {numero}")  



print(f"Quantidade de pares: {pares}")
print(f"Quantidade de impares: {impares}")