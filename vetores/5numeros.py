import os
os.system("clear")

vetor = []
negativos = 0
soma_positivos = 0

for i in range(5):
    numero = float(input(f"Digite o {i+1}º numero: "))
    vetor.append(numero)

    if numero < 0:
        negativos +=1
    else: 
        soma_positivos += numero


print("\nQuantidade de numeros negativos:", negativos)
print("Soma dos numeros positivos:", soma_positivos)