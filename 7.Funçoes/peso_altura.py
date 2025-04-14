import os
os.system("clear")

peso = float(input("Digite o seu peso: "))
altura = float(input("Digite a sua altura: "))

def calcular_imc(peso, altura):
    imc = peso / altura **2
    return imc

if calcular_imc(peso,altura) < 18.5:
    print("Abaixo do peso")
    print("Consulte um nutricionista para orientaçao")
elif calcular_imc(peso,altura) < 24.9:
    print("Peso normal")
    print("Mantenha habitos saudaveis!")
elif calcular_imc(peso,altura) < 29.9:
    print("Sobrepeso")
    print("Considere uma dieta balanceada e atividade fisica")
elif calcular_imc(peso,altura) < 34.9:
    print("Obesidade grau 1")
    print("Procure orientaçao de um profissional de saude")
elif calcular_imc(peso,altura) < 39.9:
    print("Obesidade grau 2")
    print("Consulte um medico pra avaliaçao e orientaçao")
else:
    print("Obesidade grau 3")
    print("Busque assistencia medica imediatamente")


print(f"O seu IMC e: {calcular_imc(peso,altura)}")
