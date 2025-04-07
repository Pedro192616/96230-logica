import os
os.system("clear")

def positivo_ou_negativo(numero):
    
    if numero > 0 :
        print(f"O numero e positivo.")
    elif numero < 0:
        print(f"O numero e negativo.")
    else :
        print("0 e um numero neutro.")


print("= NEGATIVO OU POSITIVO =") 
numero = int(input("Digite um numero: "))
positivo_ou_negativo(numero)