# Limpar o terminal
import os
os.system("clear")


# Elabore um algoritimo para solicitar dois numeros e ao final mostre na tela:
# O menor valor e o maior valor.

primeiro_numero = float(input("Digite o primeiro valor: "))
segundo_numero = float(input("Digite o segundo valor: "))
 


menor = min(primeiro_numero, segundo_numero)
maior = max(primeiro_numero, segundo_numero)

print(f"Menor: {menor}")
print(f"Maior: {maior}")

if primeiro_numero == segundo_numero:
   print("os números sao iguais!")