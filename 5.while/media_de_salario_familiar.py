import os
os.system("clear")

soma_de_salario = 0
contador = 0
soma_de_salario_geral = 0
    
while True:
        print("""
CODIGO | DESCRIÇAO
   1   |
   2   |
   3   |
""")

        opçao = int(input())

        match opçao :
            case 1:
                idade = int(input("Digite sua idade: "))
                sexo = input("Digite o seu sexo ? \nDigte 'F' ou 'M': ").upper()
                salario = float(input("Digite o valor do salario: "))
            case 2:
                print(f"Idade: {idade}")
                print(f"Sexo: {sexo}")
                print(f"Salario: {salario}")
            case 3:
                SystemExit
            case _:
                # Opçao invalida.


        # Processamento
                contador += 1 
                soma_de_salario_geral += salario

                media_geral_de_salario = soma_de_salario_geral / contador
        


