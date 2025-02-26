# Limpa o terminal
import os 
os.system("clear")

# Desenvolva um programa que receba como entrada um numero inteiro
# que respresente um dos 7 dias da semana e imprima na tela se:
# esse dia é util, final de semana ou invalido
# Considere que Domingo é o dia 1 e sabado o dia 7

# Entrada
dia = int(input("Digite o dia da semana: "))

# Processamento


match dia:
    case 1:
        print("domingo ")
    case 2:
        print("segunda")
    case 3:
        print("terça ")
    case 4:
        print("quarta ")
    case 5:
        print("quinta ")
    case 6:
        print("sexta ")
    case _:
        print("numero invalido!")

        print(dia)

        print("== FIM ==")
        
