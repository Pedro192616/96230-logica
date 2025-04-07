import os
os.system("clear")
    

def somar( primeiro_numero , segundo_numero):
    return primeiro_numero + segundo_numero

def subtrair( primeiro_numero , segundo_numero):
    return primeiro_numero - segundo_numero

def dividir( primeiro_numero , segundo_numero):
    return primeiro_numero / segundo_numero

def multiplicar( primeiro_numero , segundo_numero):
    return primeiro_numero * segundo_numero


primeiro_numero = int(input("Digite o primeiro numero: "))
segundo_numero = int(input("Digite o segundo numero: "))


soma = somar( primeiro_numero , segundo_numero )
subtraçao = subtrair( primeiro_numero , segundo_numero )
divisao = dividir( primeiro_numero , segundo_numero )
multiplicaçao = multiplicar( primeiro_numero , segundo_numero )

print("\n= RESULTADOS =")
print(f"Soma: {soma}")
print(f"Subtraçao: {subtraçao}")
print(f"Dvisao: {divisao}")
print(f"Multiplicaçao: {multiplicaçao}")
