import os

# Funçao sem retorno
def logo_senai():
    os.system("clear")
    print("==== SENAI ====")
    
logo_senai() # Chamando a funçao
nome = input("Digite seu nome: ")


logo_senai() # Chamando a funçao
idade= int(input("Digite sua idade: "))


logo_senai()  # Chamando a funçao  
print(f"Nome: {nome}")
print(f"Idade: {idade}")




