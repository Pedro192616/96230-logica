# Limpar o terminal
import os 
os.system ("clear")

QUANTIDADE_NOTAS = 3 
soma = 0

for i in range(QUANTIDADE_NOTAS):
    while True:
        nota = float(input("Digite uma nota: "))

        if nota < 0 or nota > 10 :
            print("Nota invalida. \nTente novamente...\n")
        else:
            soma += nota
            break

media = soma / QUANTIDADE_NOTAS

if media >= 7:
    resultado = "Aprovado."
elif media >= 5:
    resultado = "Recuperaçao"
else:
    resultado = "Reprovado."

print(f"\nMedia: {media}")
print(f"Resultado: {resultado}")