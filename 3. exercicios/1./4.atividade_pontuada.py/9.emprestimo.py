# Limpar o terminal
import os
os.system("clear")

# Entrada
renda_mensal = float(input("Digite a sua renda mensal: "))
valor_do_emprestimo = float(input("Digite o valor do emprestimo: "))
parcelas = int(input("Digite a quantidade de parcelas: "))

# Processamento
valor_max_emprestimo = renda_mensal * 10
valor_max_parcelas = renda_mensal * 0.3
valor_prestaçao = valor_do_emprestimo / parcelas

if valor_do_emprestimo > valor_max_emprestimo :
    print("Emprestimo nao concedido.")
elif parcelas > valor_max_parcelas :
    print("Emprestimo nao concedido.")
elif valor_prestaçao > renda_mensal * 0.3 :
    print("Emprestimo nao concedido.")
else :
    print("Emprestimo concedido.")

# Saida
    print(f"Valor da prestaçao: R${valor_prestaçao:.2f}")
  
