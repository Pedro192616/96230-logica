# Limpar o terminal 
import os 
os.system("clear")

# Entrada
combustivel = input("""Digite qual tipo de combustivel"
A- Alcool
G- Gasolina 
""")
preço_litro_alcool = 3.79
preço_litro_gasolina = 6.59

# Processamento

match combustivel :
    case "a" | "A" :
        litros = float(input("Digite a quantidade de litros: "))
        if litros <=25:
            desconto = 0.02
            total = preço_litro_alcool * litros
            total_a_pagar = total / desconto 

        elif litros >25 :
            desconto = 0.04
            total = preço_litro_alcool * litros 
            total_a_pagar = total / desconto

    case "g" | "G" :
        litros = float(input("Digite a quantidade de litros: "))
        if litros <=25:
            desconto = 0.03
            total = preço_litro_gasolina * litros
            total_a_pagar = total / desconto
        elif litros >25: 
            desconto = 0.05
            total= preço_litro_gasolina * litros
            total_a_pagar = total / desconto

# Saida 
print(f"Combustivel: {combustivel}")
print(f"Total a pagar: R${total_a_pagar:.2f}")



