# Limpar o terminal
import os
os.system("clear")

# Faça um programa que leia um código de operação (+,-,* ou /), e também dois valores inteiros A e B. 
# O programa deve calcular o resultado da operação escolhida aplicado a A e B. 
# Por exemplo, se a operação escolhida foi * e A = 1 e B = 3,
# o programa deve fornecer como resultado o valor de 1*3, que é 3.

# Entrada
valor_A = int(input("Digite o valor A: "))
operador = input("Digite a operaçao que deseja (+ - * /): ")
valor_B = int(input("Digite o valor B : "))

#  Processamento
match operador:
     case "*":
      resultado = valor_A * valor_B
# saida
print(f"valor A: {valor_A}")
print(f"Operaçao: {operador}")
print(f"valor B: {valor_B}")
print(f"Resultado: {resultado}")
