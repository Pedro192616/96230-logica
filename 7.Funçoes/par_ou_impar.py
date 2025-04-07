import os
os.system("clear")

def par_ou_impar(numero):

    if numero % 2 == 0:
        print(f"O numero e par.")
    else:
        print(f"O numero e impar.")

print("= PAR OU IMPAR =")
numero = int(input("Digite um numero:  "))
par_ou_impar(numero)


