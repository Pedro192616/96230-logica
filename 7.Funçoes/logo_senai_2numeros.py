import os


# Faça uma sem retorno com o nome: logo_senai()
# Limpando o terminal e inserindo: === SENAI DENDEZEIROS ===

# Solicite ao usuario dois numeros
# Cada um em uma variavel diferente
# Crie uma funçao com retorno para somar os dois numeros informados pelo usuario


def logo_senai():
    os.system("clear")
    print("==== SENAI DENDEZEIROS ====")
    

def somar( primeiro_numero , segundo_numero):
    return primeiro_numero + segundo_numero

def subtrair( primeiro_numero , segundo_numero):
    return primeiro_numero - segundo_numero

def dividir( primeiro_numero , segundo_numero):
    return primeiro_numero / segundo_numero

def multiplicar( primeiro_numero , segundo_numero):
    return primeiro_numero * segundo_numero

logo_senai()
primeiro_numero = int(input("Digite o primeiro numero: "))

logo_senai()
segundo_numero = int(input("Digite o segundo numero: "))


soma = somar( primeiro_numero , segundo_numero )
subtraçao = subtrair( primeiro_numero , segundo_numero )
divisao = dividir( primeiro_numero , segundo_numero )
multiplicaçao = multiplicar( primeiro_numero , segundo_numero )

logo_senai()
print(f"Soma: {soma}")
print(f"Subtraçao: {subtraçao}")
print(f"Dvisao: {divisao}")
print(f"Multiplicaçao: {multiplicaçao}")
