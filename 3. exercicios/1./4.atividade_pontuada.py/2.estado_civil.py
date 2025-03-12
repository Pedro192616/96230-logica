# Limpar o terminal.
import os
os.system("clear")

# Faça um algoritmo que leia o nome, o sexo e o estado civil de uma pessoa.
# Caso sexo seja “F” e estado civil seja “CASADA”, solicitar o tempo de casada (anos). 
# Por fim, mostre os dados do usuário.

# Entrada
sexo_legal = "F"
estado_civil_legal = "Casada"

Nome = input("Digite seu nome: ")
sexo = input("Digite o seu sexo: ")
estado_civil = input("Digite o seu estado civil: ")
tempo_de_casada = input

# Processamento

if sexo == sexo_legal and estado_civil == estado_civil_legal :
    tempo_de_casada = input("Digite seu tempo de casada em anos: ")
else :
    print("Estado civil ou sexo não sao legais para esse serviço. ")

# Saida
print(f"nome: {Nome}")
print(f"Sexo: {sexo_legal}")
print(f"estado civil: {estado_civil}")
print(f"tempo de casada: {tempo_de_casada}")




