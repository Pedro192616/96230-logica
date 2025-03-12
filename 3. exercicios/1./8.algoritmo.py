# Limpar o terminal 
import os
os.system("clear")

# Faça um algoritmo que solicite ao usuario dois numeros
# e um caractere que calcula as operaçoes basicas(+ - * /).
# Mostre  os numeros informados pelo usuario.
# o operador escolhido e o resultado.

# Entrada
primeiro_numero = int(input("Digite um numero: "))
operador = input("Digite a operaçao que deseja (+ - * /): ")
segundo_numero = int(input("Digte um numero: "))
resultado = input
#  Processamento
match operador:
     case "+":
      resultado = primeiro_numero + segundo_numero
# saida
print(f"\nPrimeiro numero: {primeiro_numero}")
print(f"Operaçao: {operador}")
print(f"Segundo numero: {segundo_numero}")
print(f"Resultado: {resultado}")
