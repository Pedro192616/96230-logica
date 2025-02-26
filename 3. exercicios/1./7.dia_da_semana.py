# Limpar o terminal
import os
os.system("clear")

dia = input("Digte o dia da semana: ")

match dia:
    case "segunda":
        print("Hoje é segunda feira. ")
    case "terça":
        print("Hoje é terça feira. ")
    case "quarta":
        print("Hoje é quarta feira. ")
    case "quinta":
        print("Hoje é quinta feira. ")
    case "sexta":
        print("Hoje é sexta feira. ")
    case "sabado" | "domingo":
        print("Hoje é fim de semana! ")
    case _:
          print("Dia invalido.")

print(dia)   

print("== FIM ==")