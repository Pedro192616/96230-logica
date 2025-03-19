import os
os.system("clear")

contador = 0
continua = 's'

while True:
    # Comandos a serem repetidos
    print("Repetindo....")

    continua = input("Tecle 's' se deseja continuar: ").strip().lower()
    contador +=1


    if continua != 's':
        print("O bloco NÃO foi repetido.")
    else:
        print(f"O bloco foi repetido {contador} vezes")