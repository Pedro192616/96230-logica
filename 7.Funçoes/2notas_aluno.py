import os 
os.system("clear")

def calcular (n1, n2):
    soma = n1 + n2
    return soma / 2

nota1 =float(input("Digite uma nota: "))
nota2 =float(input("Digite uma nota: "))

media = calcular(nota1, nota2)

if media >= 7:
    resultado = "Aprovado"
if media < 7:
    resultado = "Reprovado"

print(f"Media: {media}")
print(f"Resultado: {resultado}")
