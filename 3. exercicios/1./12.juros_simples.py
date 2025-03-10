# Limpar o terminal
import os 
os.system("clear")

# Solicite ao usuario para que informe o valor de um produto e a forma de pagameno:
# pagamento a vista ou pagamento a prazo

# Entrada
valor_produto = float(input("Digite o valor do produto: "))
forma_de_pagamento = int(input("""
1- A vista 
2- A prazo
Digite  a forma de pagamento: """))

match forma_de_pagamento:
    case 1:
        # Aplicando desconto de 10%.
        desconto = valor_produto * 0.10
        valor_pagar = valor_produto - desconto

        # Exibindo resultado.
        print(f"\nValor do produto: {valor_produto}")
        print(f"Forma de pagamento: a vista") 
        print(f"Valor do desconto: {desconto}")
        print(f"Total a pagar: {valor_pagar}")

    case 2:
        quantidade_parcelas = int(input("Digite a quantidade de parcelas: "))
        if quantidade_parcelas >- 1 and quantidade_parcelas <- 6:
            valor_parcela = valor_produto / quantidade_parcelas
 
           # Exibindo resultado.
            print(f"\nValor do produto: R$ {valor_produto}")
            print(f"Forma de pagamento: a prazo") 
            print(f"Quantidade de parcelas: {quantidade_parcelas}")
            print(f"Total a prazo: {valor_produto}")
        else:
            print("O parcelamento deve ser um ate 6 parcelas.")
    case _:
        print("Opçao invalida.")
