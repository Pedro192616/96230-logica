import os
import time

os.system ("cls | | clear")

numero = int(input("Digite um numero para contagem regressiva: "))

print("CONTAGEM REGRESSIVA")
for i in range (numero,0,-1):
    print(f"Valor de variavel i: {i}")
    time.sleep(1)

print("FIM DO PROGRAMA")