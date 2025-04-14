import os
os.system("clear")

lista_numeros = []
QUANTIDADE_NUMEROS = 5

print("= Solicitando numeros =")
for i in range(QUANTIDADE_NUMEROS):
    numero = float(input(f"Digite o {i+1}º numero: "))
    lista_numeros.append(numero)

# Verificando maior e menor numeros em uma lista.
# As funçoes max() e min() percorrem o vetor e mostram o maior e
# O menor numero respectivamnete.
menor = min(lista_numeros)
maior = max(lista_numeros)

print("\nMostrando numeros: ")
# Usando ForEach numerando os elementos da lista
# Iniciando contagem com a variavel i, começando com o numero 1.
for i,numero in enumerate(lista_numeros, start=1):
     print(f"{i}º numero: {numero}")  


print(f"\nMaior numero: {maior}")
print(f"\nMenor numero: {menor}")


