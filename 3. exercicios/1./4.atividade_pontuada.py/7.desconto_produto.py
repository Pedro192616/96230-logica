# Limpar o terminal
import os
os.system("clear")

# Entrada

produto = input("Digite o nome do produto: ")
quantidade_adquirida = int(input("Digite a quantidade adquirida: "))
preço_unitario = int(input("Digite o preço unitario: "))
desconto = float
# Processamento
total = quantidade_adquirida * preço_unitario

if quantidade_adquirida <= 5:
    desconto = 0.02
    total_a_pagar = total - desconto
elif quantidade_adquirida >5 and quantidade_adquirida <=10 :
    desconto = 0.03
    total_a_pagar = total - desconto 
elif quantidade_adquirida >10 :
    desconto = 0.05

# saida
print(f"Produto: {produto}")
print(f"Preço unitario: {preço_unitario:.2f}")
print(f"Quantidade adquirida: {quantidade_adquirida}")
print(f"Total a pagar: {total_a_pagar}")


