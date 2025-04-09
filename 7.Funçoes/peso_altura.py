import os
os.system("clear")

peso = float(input("Digite o seu peso: "))
altura = float(input("Digite a sua altura: "))

def calcular_inc(peso, altura):
    inc = peso / altura **2
    return inc

if calcular_inc(peso,altura) < 18.5:
    print("Abaixo do peso")
elif calcular_inc(peso,altura) < 24.9:
    print("Peso normal")
elif calcular_inc(peso,altura) < 29.9:
    print("Sobrepeso")
elif calcular_inc(peso,altura) < 34.9:
    print("Obesidade grau 1")
elif calcular_inc(peso,altura) < 39.9:
    print("Obesidade grau 2")
else:
    print("Obesidade grau 3")


print(f"O seu INC e: {calcular_inc(peso,altura)}")
