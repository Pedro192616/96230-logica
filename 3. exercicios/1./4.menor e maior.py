# Limpar o terminal
import os
os.system("clear")

primeiro_numero = float(input("Digite a primeira nota: "))
segundo_numero = float(input("Digite a segunda nota: "))

media = (primeiro_numero + segundo_numero)
produto = primeiro_numero * segundo_numero

if primeiro_numero < segundo_numero:
   
    menor = primeiro_numero 
    maior = segundo_numero
else:
    menor = segundo_numero
    maior = primeiro_numero

print("\nExibindo resultados: ")
print(f"Media: {media}")
print(f"Produto: {produto}")
print(f"Menor: {menor}")
print(f"Maior: {maior}")