import os
import time
os.system("clear")


# Lista de nomes
lista_nomes = []

# Funçao para verificar se a lista esta vazia.
def verificar_lista_vazia(lista_nomes):
    if not lista_nomes:
        return True
    return False

# Funçao para adicionar.
def adicionar_nome(lista_nomes):
    nome = input("Digite o nome que deseja adicionar: ")
    lista_nomes.append(nome)
    print(f"\n{nome} adicionado com sucesso.")

# Funçao para mostrar todos os nomes da lista.
def listar_nomes(lista_nomes):
    # Verificar se a lista esta vazia.
    if verificar_lista_vazia(lista_nomes):
        return
    
    print("\n Lista de nomes ")
    for nome in lista_nomes:
        print(f"- {nome}")

# Mostrando menu.
while True:
    print("""
    - Gerenciador de nomes -
    1 - Adicionar
    2 - Listar nomes
    3 - Atualizar
    4 - Remover
    5 - Sair
    """)
    opcao = int(input("Digite uma das opçoes acima: "))

    match opcao:
        case 1:
            adicionar_nome(lista_nomes)
        case 2:
            listar_nomes(lista_nomes)
        case 3:
            ...
        case 4:
            ...
        case 5:
            print("\nSaindo do programa.")
        case 6:
            print("\nOpçao invalida.\nTente novamente.")
    time.sleep(5) 
    
