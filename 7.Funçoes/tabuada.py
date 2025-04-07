import os 
os.system("clear")

def tabuada(numero):
    for i in range(0,11):
        print (f"{numero} x {i} = {numero * i}")

numero = int(input("Digite um numero da tabuada de 1 a 10: "))

if 1 <= numero <= 10:
    tabuada(numero)
else:
    print("Digite um numero de 1 a 10.")

print("FIM DO PROGRAMA")
