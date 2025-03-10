# Limpar o terminal.
import os
os.system("clear")

# Entrada
matricula = int(input("Digite a matricula: "))
ano_de_nascimento = int(input("Digite o ano de nascimento: "))
anos_de_trabalho = int(input("Digite o tempo de trabalho: "))
ano_atual = int(input("Digite o ano atual: "))

# Processamento
idade =  ano_atual - ano_de_nascimento
soma = idade + anos_de_trabalho

if soma >= 95 :
    conceito =  "A"
elif soma < 95 :
    conceito = "B"

match conceito:
    case "A" :
        print("Requerer apsentadoria.")
    case "B" :
        print("Nao requerer aposentadoria.")
    case _:
        print("opçao invalida.")