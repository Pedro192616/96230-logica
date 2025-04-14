import os
os.system("clear")

lista_numeros = []
QUANTIDADE_NOTA = 4


for i in (QUANTIDADE_NOTA):
    nota = float(input("Digite uma nota: "))
    lista_numeros.append(nota)

media = sum(lista_numeros) / QUANTIDADE_NOTA

if media >= 7:
    resultado = "Aprovado"
if media >= 5:
     resultado = "Recuperaçao"
if media <= 4:
    resultado = "Reprovado"
        
        

print()
for nota in lista_numeros:
    print(nota)


print(f"Media: {media}")
print(f"Resultado: {resultado}")
