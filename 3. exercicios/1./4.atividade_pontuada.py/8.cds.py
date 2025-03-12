# Limpar o terminal
import os 
os.system("clear")
# Em uma loja de CD´s existem apenas quatro tipos de preços que estão associados a cores.
# Assim os CD´s que ficam na loja não são marcados por preços e sim por cores. 
# Desenvolva o algoritmo que a partir da entrada da cor o software mostre o preço.
# A loja está atualmente com a seguinte tabela de preços.  # Entrada

# Entrada
opçao = int(input("""
1 \t verde \t\t R$ 10,00
2 \t azul \t\t R$ 20,00
3 \t amarelo \t\t R$ 30,00
4 \t vermelho \t\t R$ 40,00
Digite a opçao desejada:
"""))

# Processamento
match opçao:
    case 1:
        print("verde - R$ 10,00.")
    case 2:
        print("azul - R$ 20,00.")
    case 3:
        print("amarelo - R$ 30,00.")
    case 4:
        print("vermelho - R$ 40,00.")
    case _:
        print("opçao invalida!")
    # Saida