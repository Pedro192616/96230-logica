import os
os.system("clear")

lista_pratos = []
precos_pratos = []

while True :
     
    print("""
    ===================== MENU =======================      
    Codigo \t Prato \t\t\t Preço
    1 \t Picanha \t\t R$ 25,00
    2 \t Lasanha \t\t R$ 15,00
    3 \t Strogonoff \t\t R$ 18,00
    4 \t Bife acebolado \t R$ 20,00                
    5 \t Pão com ovo \t\t R$ 5,00
    """)

    opçao = int(input("Digite o numero da opçao desejada: "))
    

    match opçao:
        case 1:
            prato = "Picanha"
            preço = 25
        case 2:
            prato = "Lasanha"
            preço = 20 
        case 3:
            prato = "Strogonoff"
            preço = 18
        case 4:
            prato = "Bife acebolado"
            preço = 15
        case 5:
            prato = "pão com ovo"
            preço = 5
        case _:
            prato = "opçao invalida!"
            preço = 0 

    lista_pratos.append(prato)
    precos_pratos.append(preço)

    repetir = input("Deseja escolher outro prato? \nDigte 'S' ou 'N': ").lower()
    if repetir == "n":
        break


print("= PRATOS ESCOLHIDOS =")
for prato in lista_pratos:
    print(f"Prato: {prato}")

print(f"Total a pagar: R$ {precos_pratos}")