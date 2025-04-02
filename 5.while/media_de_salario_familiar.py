import os
import time

soma_de_salario = 0
contador = 0
soma_de_salario_geral = 0
maior_idade = 0
menor_idade = 9999
mulheres5k = 0
    
while True:
        print("""
CODIGO | DESCRIÇAO
   1   |    Adicionar pessoa
   2   |    Exibir resultado    
   3   |    Sair
""")

        opçao = int(input())

        match opçao :
            case 1:
                idade = int(input("Digite sua idade: "))
                sexo = input("Digite o seu sexo ? \nDigte 'F' ou 'M': ").upper()
                salario = float(input("Digite o valor do salario: "))
                contador += 1 
                soma_de_salario += salario
                maior_idade = max(maior_idade, idade)
                menor_idade = min(menor_idade, idade)
                if sexo == "F" and salario >= 5000:
                     mulheres5k += 1
                
            case 2:
                if contador > 0:
                    media_salarial = soma_de_salario / contador
                    print(f"Media salarial do grupo: {media_salarial}")
                    print(f"Maior idade do grupo: {maior_idade}")
                    print(f"Menor idade do grupo: {menor_idade}")
                    print(f"Quantidade de mulheres com salario a partir de 5k: {mulheres5k}")
                else:
                    print("\nNao foram informados os dados necessarios.")
                time.sleep(3)
                os.system("clear")
                break
                
            case 3:
                print("\n= FIM =")