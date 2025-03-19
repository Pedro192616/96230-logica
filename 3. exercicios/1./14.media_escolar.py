# Limpa terminal
import os 
os.system("clear")

# Entrada
nome = input("Digite o nome do aluno: ")
primeira_nota = float(input("Digite a primeira nota: "))
segunda_nota = float(input("Digite a segunda nota: "))
                           
if nome :
    conceito = "A" | "B" | "C"
else :
    conceito = "D" | "E"

match conceito:
    case "A" | "B" | "C":
        print(f"Conceito: {conceito}")
        print("Aprovado.")
    case "D" | "E" :
        print(f"Conceito: {conceito}")
        print("Reprovado.")
    case _:
        print("opçao invalida.")


