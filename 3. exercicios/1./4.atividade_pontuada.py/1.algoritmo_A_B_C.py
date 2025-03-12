# Limpar o terminal
import os 
os.system("clear")

#Faça um algoritmo que leia os valores A, B, C e imprima na tela se a soma de A + B é menor que C.
# caso contrário, imprima que a A + B é maior que C. 

# Entrada
valor_A = float(input("Digite o valor A: "))
valor_B = float(input("Digite o valor B: "))
valor_C = float(input("Digite O valor C: "))

# Processamento

soma = valor_A + valor_B
soma < valor_C

if soma < valor_C :
    print("A soma de A+B É menor que C!")
elif soma > valor_C :
    print("A soma de A+B É maior que C!")